from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    articles = models.Article.objects.all()
    # type(articles)
    return render(request,'blog/index.html',{'article':articles})
