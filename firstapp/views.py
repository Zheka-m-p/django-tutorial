from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


def home(request): # Главная страница
    context = {
        "title": "Главная страница",
        "user": "Евгений",
    }
    return render(request, 'firstapp/home.html', context)

def about(request): # О сайте, о нас - добавили Шаблон html-формата, вместо обычного текста
    return render(request, 'firstapp/about.html')

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

def developer(request): # Страница о разработчике
    return HttpResponse("<h2>Разработчик: Евгений Черников</h2>")

# в другой день
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

# про редирект
def redirect_example(request): # пример простого редиректа
    return HttpResponseRedirect('/about')

def permanently_redirect_example(request):
    return HttpResponsePermanentRedirect('https://abilityarena.com/')

# про редирект еще способы - redirect
def go_to_about(request):
    return redirect('about')  # ← имя маршрута, а не строка '/about/', можно и на сайт просто "https://example.com"

def redirect_to_profile(request, user_id): # редирект на страницу конкретного пользователя по его айди
    return redirect('user_detail', user_id=user_id)

# про статус код кастомные
def forbidden_view(request): #  переход на 404 страницу со статус кодом 403
    return HttpResponse("Доступ запрещён: status_code = 403", status=403)


# начинаем копыхаться с шаблонами и переданными в них контекстами (context)
def users_list(request): # вывод списка через цикл for - смотреть в шаблоне
    context = {
        "users": ["Андрей", "Мария", "Сергей", "Анна"]
    }
    return render(request, 'firstapp/users_list.html', context)


def user_info(request): # вывод через словарь - смотреть в шаблоне
    context = {
        "user": {"name": "Жека", "age": '18+', "city": "Питер"}
    }
    return render(request, 'firstapp/profile.html', context)

def check_age(request):
    context = {"age": 20}
    return render(request, 'firstapp/age.html', context)