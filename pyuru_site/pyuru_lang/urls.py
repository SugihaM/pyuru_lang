from django.urls import path

from . import views

app_name = 'pyuru_lang'
urlpatterns = [
    path('', views.index, name='index'),
    path('input_ja/', views.input_text, name='input'),
    path('result/', views.result, name='result'),
]
