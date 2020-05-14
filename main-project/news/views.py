from django.shortcuts import render
from news.models import News


def index_page(request):
    """ Стартовая страница """

    context = {}
    news = News.objects.all()

    context['title'] = 'Всі новини'
    context['news'] = news
    
    return render(request, 'news/index_page.html', context)