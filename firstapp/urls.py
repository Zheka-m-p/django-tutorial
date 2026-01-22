from django.urls import path
from . import views # Импортируем views из текущей папки

urlpatterns = [
    path('', views.index, name='home'),  # Привязываем корневой маршрут к представлению index - Главная страница
    path('about/', views.about, name='about'),  # Страница "О нас"
    path('contact/', views.contact, name='contact'),  # Страница "Контакты"

    path('user_detail/<int:user_id>', views.user_detail, name='user_detail'),  # Динамическая страница пользователя
    path('product_detail/<int:id>/<str:category>/', views.product_detail, name='product_detail'), # Передавать можно два параметра динамически

    path('products/', views.filter_products, name='filter_products'), # тестируем GET запрос и передачу параметров
    path('filter-price/', views.filter_by_price, name='filter-price'), # тестируем два параметра в GET-запросе
    path('check_age/', views.check_age, name='check_age'), # проверка на возраст для практики
    path('articles/', views.filter_articles, name='filter_articles'), # на получение списка практика

    path('redirect_example/', views.redirect_example, name='redirect_example'), # пример простого редиректа
    path('permanently_redirect_example/', views.permanently_redirect_example, name='permanently_redirect_example'), # пример перманентного редиректа
]