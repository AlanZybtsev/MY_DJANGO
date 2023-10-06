
from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os


# Create your views here.
def MAIN(request):
    return HttpResponse('Cтраница приложения MAIN.')


def categories(request, catid):
    print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям.</h1><p>{catid}</p>')

def home_view(request):
    return HttpResponse('Главная страница сайта MAIN.')

def archive(request, year):
    return HttpResponse(f'<h1>Архив по годам</h1></h1><p>{year}</p>')