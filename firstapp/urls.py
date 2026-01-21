from django.urls import path
from . import views # Импортируем views из текущей папки

urlpatterns = [
    path('', views.index, name='home'),  # Привязываем корневой маршрут к представлению index - Главная страница
    path('about/', views.about, name='about'),  # Страница "О нас"
    path('contact/', views.contact, name='contact'),  # Страница "Контакты"
    path('user_detail/<int:user_id>', views.user_detail, name='user_detail'),  # Динамическая страница пользователя
    path('product_detail/<int:id>/<str:category>/', views.product_detail, name='product_detail'), # Передавать можно два параметра динамически
]