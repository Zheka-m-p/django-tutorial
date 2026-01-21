from django.shortcuts import render
from django.http import HttpResponse
from unicodedata import category


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

# в другой день
def filter_products(request): # тестируем get запрос и передачу параметров
    category = request.GET.get('category', '')
    if category:
        return HttpResponse(f'Выбрана категория: {category}')
    return HttpResponse('Категория не выбрана')

def filter_by_price(request): # тестируем два параметра в GET-запросе
    d = request.GET.dict()
    if 'min_price' in d and 'max_price' in d:
        min_price = d.get('min_price')
        max_price = d.get('max_price')
        return HttpResponse(f"Товары в диапазоне {min_price} - {max_price}")
    else:
        return HttpResponse("Не указан диапазон цен")

def check_age(request):
    age = request.GET.get('age', '')
    if age:
        try:
            age = int(age)
        except ValueError:
            return HttpResponse('Ввели некорректное значение для возраста')
        if age >= 18:
            return HttpResponse('Доступ разрешен')
        else:
            return HttpResponse('Доступ запрещен')

    return HttpResponse("Возраст не указан")

def filter_articles(request): # # на получение списка практика
    lst = request.GET.getlist('tags')
    if lst:
        return HttpResponse(f'Статьи с тегами: {', '.join(lst)}')
    return HttpResponse('Теги не выбраны')