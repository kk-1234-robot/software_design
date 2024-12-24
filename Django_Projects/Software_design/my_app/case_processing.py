import nltk
from my_app.models import Train, Sentences, Words

nltk.download('punkt')

#每次读取第n行的Train数据,返回第m个case
def read_train_data(n, m):
    train = Train.objects.get(id=n)
    if m == 1:
        return train.case1
    elif m == 2:
        return train.case2
    elif m == 3:
        return train.case3
    else:
        return "No such case in Train table."

#将一个case分成句子并返回句子数量以及句子列表
def split_sentence(case):
    sentences = nltk.sent_tokenize(case)
    return len(sentences), sentences

#将第n个句子分成单词并返回单词数量以及单词列表
def split_word(sentence):
    words = nltk.word_tokenize(sentence)
    return len(words), words


#将得到的句子列表中的每个句子存入数据库中的Sentences表中
def save_sentences(sentences):
    for sentence in sentences:
        s = Sentences(sentence=sentence)
        s.save()


#将得到的单词列表中的每个单词存入数据库中的Words表中，重复的单词count加1
def save_words(words):
    for word in words:
        try:
            w = Words.objects.get(word=word)
            w.count += 1
            w.save()
        except Words.DoesNotExist:
            w = Words(word=word, count=1)
            w.save()
