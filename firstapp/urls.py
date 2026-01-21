from django.urls import path
from . import views # Импортируем views из текущей папки

urlpatterns = [
    path('', views.index, name='index'),  # Привязываем корневой маршрут к представлению index
    path('about/', views.about, name='about'),  # Страница "О нас"
]