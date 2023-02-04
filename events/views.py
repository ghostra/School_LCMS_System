from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from . import forms


def event_list(request):
    articles = Article.objects.all().order_by('date');
    return render(request, 'events/event_list.html', { 'articles': articles })

def event_detail(request, slug):
    # return HttpResponse(slug)

    article = Article.objects.get(slug=slug);
    return render(request, 'events/event_detail.html', {'article': article})
