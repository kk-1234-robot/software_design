from django.shortcuts import render
from django.http import HttpResponse

from my_app.case_processing import read_train_data
from my_app.models import Train


# Create your views here

# 返回第n行第m个case的数据,n 为 number 除以3的商，m 为 number 除以3的余数
def view_train(request):
    number = request.GET.get('number')
    if number:
        try:
            number = int(number)
            n = number // 3 + 1
            m = number % 3 + 1
            case = read_train_data(n, m)
            return HttpResponse(case, content_type="text/plain;charset=utf-8")
        except ValueError:
            return HttpResponse("invalid input number.", content_type="text/plain;charset=utf-8")
    else:
        return HttpResponse("Please input number.", content_type="text/plain;charset=utf-8")
