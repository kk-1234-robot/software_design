from django.shortcuts import render
from django.http import HttpResponse
from django.utils.text import normalize_newlines
from rest_framework.decorators import api_view

from my_app.case_processing import read_train_data, get_words_db
from my_app.case_processing import split_into_sentences
from my_app.models import Train
import csv
from django.core.files import File


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


def get_words(request):
    number = request.GET.get('number')
    num_sentences = request.GET.get('num_sentences')
    num_words = request.GET.get('num_words')
    print('get_word_test')
    if num_words and number and num_sentences:
        print('get_word_test')
        try:
            num_sentences = int(num_sentences)
            number = int(number)
            num_words = int(num_words)
            print('get_word_test')
            word = get_words_db(number, num_sentences, num_words)
            return HttpResponse(word, content_type="text/plain;charset=utf-8")
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
    return HttpResponse("Received", content_type="text/plain;charset=utf-8")


@api_view(['POST'])
# 获取前端提交的任务数据(文件为.csv文件),并将其存入数据库中的Test表
def get_task(request):
    file = request.FILES['file']
    reader = csv.reader(file)
    for row in reader:
        t = Train(case1=row[0], case2=row[1], case3=row[2])
        print(t)
        t.save()
    return HttpResponse("Received", content_type="text/plain;charset=utf-8")
