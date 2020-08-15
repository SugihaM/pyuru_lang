from django.urls import path
import os 

from . import views

app_name = 'pyuru_lang'
urlpatterns = [
    path('', views.index, name='index'),
    path(os.path.join('input_ja', ''), views.input_text, name='input'),
    path(os.path.join('result', ''), views.result, name='result'),
]
