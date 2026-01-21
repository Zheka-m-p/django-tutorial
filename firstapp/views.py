from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World! Это мой первый проект на Django!")


def about(request):
    return HttpResponse("Контакты, О нас, и многое другое!")