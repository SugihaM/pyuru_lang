from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from . import forms

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
