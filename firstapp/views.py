from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Главная</h2>")

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

def user_detail(request, user_id):
    return HttpResponse(f"<h2>Пользователь с ID: {user_id}</h2>")

def product_detail(request, id, category):
    return HttpResponse(f'<h2>Товар {id} в категории "{category}"</h2>')