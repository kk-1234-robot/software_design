import json

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.text import normalize_newlines
from rest_framework.decorators import api_view

from my_app.case_processing import *
from my_app.case_processing import split_into_sentences
from my_app.llm_api import *
from my_app.models import Train, TestCases
import csv
from django.core.files import File
import pandas as pd


# Create your views here

# 返回第n行第m个case的数据,n 为 number 除以3的商，m 为 number 除以3的余数
def view_train(request):
    number = request.GET.get('number')
    if number:
        try:
            number = int(number)
            n = (number - 1) // 3 + 1
            m = number % 3
            case = read_train_data(n, m, number)
            return HttpResponse(case, content_type="text/plain;charset=utf-8")
        except ValueError:
            return HttpResponse("invalid input number.", content_type="text/plain;charset=utf-8")
    else:
        return HttpResponse("Please input number.", content_type="text/plain;charset=utf-8")


# 通过调用split_into_sentences函数，对指定的句子进行分割
def split_sentences(request):
    number = request.GET.get('number')
    num_sentences = request.GET.get('num_sentences')
    print('test')
    if number and num_sentences:
        try:
            number = int(number)
            num_sentences = int(num_sentences)
            sentence = split_into_sentences(number, num_sentences)
            if num_sentences:
                return HttpResponse(sentence, content_type="text/plain;charset=utf-8")
            else:
                return HttpResponse("The number of sentences is less than the input number.",
                                    content_type="text/plain;charset=utf-8")
        except ValueError:
            return HttpResponse("invalid input number.", content_type="text/plain;charset=utf-8")
    else:
        return HttpResponse("Please input number and num_sentences.", content_type="text/plain;charset=utf-8")


# 通过调用get_words_db函数，获取指定位置的词语及对应的词性和实体
def get_words(request):
    number = request.GET.get('number')
    num_sentences = request.GET.get('num_sentences')
    num_words = request.GET.get('num_words')
    if num_words and number and num_sentences:
        try:
            num_sentences = int(num_sentences)
            number = int(number)
            num_words = int(num_words)
            print('get_word_test')
            data = get_words_db(number, num_sentences, num_words)
            word = data[0]
            pos = data[1]
            entity = data[2]
            print('word:', word)
            print('pos:', pos)
            print('entity:', entity)
            data = json.dumps(data)
            return HttpResponse(data,
                                content_type="application/json;charset=utf-8")
        except ValueError:
            return HttpResponse("invalid input number_sentence.", content_type="text/plain;charset=utf-8")
    else:
        return HttpResponse("Please input number_sentence, number and num_words.",
                            content_type="text/plain;charset=utf-8")


# 通过调用translate_sentence_db函数，对指定的句子进行翻译
def translate_sentence(request):
    number = request.GET.get('number')
    num_sentences = request.GET.get('num_sentences')
    if number and num_sentences:
        try:
            num_sentences = int(num_sentences)
            number = int(number)
            eng_sentence = translate_sentence_db(number, num_sentences)
            return HttpResponse(eng_sentence, content_type="text/plain;charset=utf-8")
        except ValueError:
            return HttpResponse("invalid input number_sentence.", content_type="text/plain;charset=utf-8")
    else:
        return HttpResponse("Please input number_sentence, number and num_words.",
                            content_type="text/plain;charset=utf-8")


# 通过调用llm_api.py中的函数，对指定的句子进行标注
def annotation_by_llm(request):
    number = request.GET.get('number')
    num_sentences = request.GET.get('num_sentences')
    # 调用annotation_ai_pos和annotation_ai_entity函数，对指定的句子进行标注
    if number and num_sentences:
        try:
            num_sentences = int(num_sentences)
            number = int(number)
            annotation_ai_pos(number, num_sentences)
            annotation_ai_entity(number, num_sentences)
            return HttpResponse("标注成功", content_type="text/plain;charset=utf-8")
        except ValueError:
            return HttpResponse("invalid input number_sentence.", content_type="text/plain;charset=utf-8")
    else:
        return HttpResponse("Please input number_sentence, number and num_words.",
                            content_type="text/plain;charset=utf-8")


@api_view(['POST'])
# 获取前端提交的数组数据
def get_submission(request):
    payload = request.data
    print(payload)
    # 将前端提交的数据保存到数据库中
    save_annotation_db(payload)
    return HttpResponse("Received", content_type="text/plain;charset=utf-8")


@api_view(['POST'])
# 获取前端提交的任务数据(文件为.csv文件),读取文件内容并提取出每一行的数据
def get_task(request):
    # 获取前端提交的文件
    file = request.FILES['file']
    print(file)
    print(file.name)
    print(file.size)
    print(file.content_type)
    print('hello')
    # 读取文件内容,并将其中每一行中的数据存入Test表中
    df = pd.read_csv(file, encoding='utf-8')
    for index, row in df.iterrows():
        print(row['case1'])
        case1 = row['case1']
        case2 = row['case2']
        case3 = row['case3']
        t = TestCases(case1=case1, case2=case2, case3=case3)
        t.save()

    return HttpResponse("Received", content_type="text/plain;charset=utf-8")


# 统计数据库中words表中的数据并返回包含各个词性（n,v,adj,prep,pron）的总数量
def get_pos_data(request):
    # 得到数据库中的词性数量
    num_n = Words.objects.filter(pos='n').count()
    num_v = Words.objects.filter(pos='v').count()
    num_adj = Words.objects.filter(pos='adj').count()
    num_prep = Words.objects.filter(pos='prep').count()
    num_pron = Words.objects.filter(pos='pron').count()
    data = [num_n, num_v, num_adj, num_prep, num_pron]
    data = json.dumps(data)
    print('posData:', data)
    return HttpResponse(data, content_type="application/json;charset=utf-8")


# 统计数据库中words表中的数据并返回各个实体(person,time,location)的数量
def get_entity_data(request):
    # 得到数据库中的实体数量
    num_person = Words.objects.filter(entity='person').count()
    num_time = Words.objects.filter(entity='time').count()
    num_location = Words.objects.filter(entity='location').count()
    data = [num_person, num_time, num_location]
    data = json.dumps(data)
    print('entityData:', data)
    return HttpResponse(data, content_type="application/json;charset=utf-8")


@api_view(['POST'])
# 获取前端更新的文本以及对应的article_id，更新数据库中的Train表
def update_case(request):
    payload = request.data
    text = payload['text']
    number = payload['number']
    n = (number - 1) // 3 + 1
    m = number % 3
    # 将数据库中的Train表中的对应case更新为前端提交的文本
    train = Train.objects.get(id=n)
    if m == 0:
        train.case1 = text
    elif m == 1:
        train.case2 = text
    elif m == 2:
        train.case3 = text
    train.save()
    # 将sentence表中的对应句子删除
    sentences = Sentences.objects.filter(article_id=number)
    for sentence in sentences:
        sentence.delete()
    # 将words表中的对应单词删除
    words = Words.objects.filter(article_id=number)
    for word in words:
        word.delete()
    print('update success article_id:', number)
    return HttpResponse("Received", content_type="text/plain;charset=utf-8")


def split_words(request):
    number = request.GET.get('number')
    num_sentences = request.GET.get('num_sentences')
    if number and num_sentences:
        try:
            num_sentences = int(num_sentences)
            number = int(number)
            sentence = split_words_db(num_sentences, number)
            return HttpResponse(sentence, content_type="text/plain;charset=utf-8")
        except ValueError:
            return HttpResponse("invalid input number_sentence.", content_type="text/plain;charset=utf-8")
    else:
        return HttpResponse("Please input number_sentence, number and num_words.",
                            content_type="text/plain;charset=utf-8")


# 将数据库中的sentence表和word表中的数据导出为.csv文件，导出前清除原始文件中的数据
def export_data(request):
    sentences = Sentences.objects.all()
    words = Words.objects.all()
    # 将数据库中的sentence表和word表中的数据导出为.csv文件
    with open('sentences.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['sentence', 'emotion', 'translation', 'article_id', 'pos_index'])
        for sentence in sentences:
            writer.writerow(
                [sentence.sentence, sentence.emotion, sentence.translation, sentence.article_id,
                 sentence.pos_index])
    with open('words.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['word', 'pos', 'entity', 'count', 'article_id', 'sentence_id', 'pos_index'])
        for word in words:
            writer.writerow([word.word, word.pos, word.entity, word.count, word.article_id, word.sentence_id,
                             word.pos_index])

    return HttpResponse("Received", content_type="text/plain;charset=utf-8")
