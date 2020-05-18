from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Category
from news.froms import NewsForm

def index_page(request):
    """ Стартова сторінка """

    context = {}
    news = News.objects.all()
    categories = Category.objects.all()

    context['title'] = 'Всі новини'
    context['news'] = news
    
    return render(request, 'news/index_page.html', context)


def get_category(request, category_id):
    """ Новини конкретної категорії """

    context = {}
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = categories.get(pk=category_id)
    context['news'] = news
    context['current_category'] = category

    return render(request, 'news/news_category.html', context)


def view_news(request, news_id):
    """ Перегляд конкретної новини """

    context = {}
    news_item = get_object_or_404(News, pk=news_id)
    context['news_item'] = news_item
    return render(request, 'news/view_news.html', context)


def add_news(request):
    """ Створення новини """

    context = {}
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = News.objects.create(**form.cleaned_data)
            return redirect('news:view-news', news_id = news.id)
        context['form'] = form
    else:
        form = NewsForm()
        context['form'] = form
    return render(request, 'news/add_news.html', context)