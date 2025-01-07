import nltk
from my_app.models import Train, Sentences, Words
import jieba as jb
import re
from .llm_api import *

nltk.download('punkt')

chinese_punctuation = "！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣、〃《》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰–—‘’‛“”„‟…‧。"  # 注意这里添加了全角句号“。”


# 每次读取第n行的Train数据,返回第m个case
def read_train_data(n, m, number):
    train = Train.objects.get(id=n)
    if m == 0:
        save_data(train.case1, number)
        return train.case1
    elif m == 1:
        save_data(train.case2, number)
        return train.case2
    elif m == 2:
        save_data(train.case3, number)
        return train.case3
    else:
        return "No such case in Train table."


# 将得到的单词列表中的每个单词存入数据库中的Words表中，重复的单词count加1,不保存标点符号
def save_words(words, article_id, sentence_id):
    print('saving words')
    for i, word in enumerate(words):
        try:
            w = Words.objects.get(word=word, article_id=article_id, sentence_id=sentence_id, pos_index=i + 1)
            w.count += 1
            w.save()
        except Words.DoesNotExist:
            w = Words(word=word, count=1, article_id=article_id, sentence_id=sentence_id, pos_index=i + 1)
            w.save()


# 将长文本按句子分割并存入数据库，并将句子总数num一并返回
def save_data(case, article_id):  # 这个函数的输入是一段长文本，返回值是长文本按句子分得的向量
    # 匹配中文句子结尾符号：。！？
    sentence_endings = r'[。！？]'
    sentences = re.split(f'({sentence_endings})', case)

    # 将句子和它们的结束符号重新组合在一起，并去除空字符串
    combined = []
    for i in range(0, len(sentences) - 1, 2):
        if sentences[i] or sentences[i + 1]:
            combined.append(sentences[i] + sentences[i + 1])

    # 如果最后一个元素不是结束符，则添加
    if len(sentences) % 2 != 0 and sentences[-1]:
        combined.append(sentences[-1])

    # 将句子存入数据库，若数据库中已有该句子，则不再存入
    for i, sentence in enumerate(combined):
        if not Sentences.objects.filter(pos_index=i + 1, article_id=article_id):
            s = Sentences(sentence=sentence, article_id=article_id, pos_index=i + 1)
            s.save()
            # 去掉句子中的标点符号以及换行符
            sentence = re.sub(rf'[{chinese_punctuation}]', '', sentence)
            # 将句子分词后存入Words表
            words = jb.cut(sentence)
            save_words(words, article_id, i + 1)
            print(f"Saved sentence {i + 1}: {sentence}")

    return combined, len(combined)


def split_into_sentences(number, num_sentences):
    # 返回第number个case的第num_sentences个句子
    sentence = Sentences.objects.filter(article_id=number, pos_index=num_sentences)
    # 返回Sentences表中的sentence字段
    return sentence[0].sentence


# 从数据库中取出Words中的数据
def get_words_db(number, number_sentence, num_words):
    word = Words.objects.filter(sentence_id=number_sentence, article_id=number, pos_index=num_words)
    print(word)
    return [word[0].word, word[0].pos, word[0].entity]


# 将单个句子翻译成英文
def translate_sentence_db(number, number_sentence):
    sentence = Sentences.objects.filter(pos_index=number_sentence, article_id=number)
    eng_sentence = translate_by_api(sentence[0].sentence)
    return eng_sentence


# 把标注的结果保存到数据库中,annotation是一个字典,selectedA以及selectedB是一个数组，去除其中的空字符串并分别赋值给pos和entity
def save_annotation_db(annotation):
    word = Words.objects.filter(sentence_id=annotation['num_sentences'], article_id=annotation['number'],
                                pos_index=annotation['num_words'])
    word = word[0]
    selected_a = annotation['selectedA']
    selected_b = annotation['selectedB']
    for i in selected_a:
        if i != '':
            word.pos = i
            break
    for i in selected_b:
        if i != '':
            word.entity = i
            break
    word.save()


def annotation_ai_pos(number, number_sentence):
    words = Words.objects.filter(sentence_id=number_sentence, article_id=number)
    for word in words:
        annotation_pos = annotation_pos_by_api(word.word)
        if annotation_pos != 'other':
            word.pos = annotation_pos
        else:
            word.pos = ''
        word.save()


def annotation_ai_entity(number, number_sentence):
    words = Words.objects.filter(sentence_id=number_sentence, article_id=number)
    for word in words:
        annotation_pos = annotation_entity_by_api(word.word)
        if annotation_pos != 'other':
            word.entity = annotation_pos
        else:
            word.entity = ''
        word.save()
