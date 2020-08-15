from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from . import forms, pyuru_kai

# Create your views here.
def index(request):
    return render(request, 'pyuru_lang/index.html')

def input_text(request):
    form = forms.HelloForm(request.GET or None)
    if form.is_valid():
        message = ''
    else:
        message = ''

    d = {
        'form': form,
        'message': message,
    }

    return render(request, 'pyuru_lang/input_text.html', d)

def result(request):
    p = pyuru_kai.Pyuru_Lang_Translation()
    string = request.POST['your_name']
    translation_string = p.pyuru_lang_translation(string)

    d = {
        'label': 'ぴゅる語翻訳結果',
        'message':string,
        'translation_message':translation_string,
    }

    return render(request, 'pyuru_lang/result.html', d)
