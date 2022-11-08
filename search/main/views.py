from django.shortcuts import render
from django.http import request
from .searcher import search


def index(request):
    return render(request, 'main/index.html')


def srch(request):
    word = str(request.GET['search'])
    list = search(word)
    return render(request, 'main/srch.html', context={'list': list})


def full_text(request):
    return render(request, 'main/full_text.html')


