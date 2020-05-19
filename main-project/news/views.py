from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Category
from news.froms import NewsForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


class HomeNews(ListView):
    """ Всі новини """

    model = News
    template_name = 'news/index_page.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Всі новини'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsByCategory(ListView):
    """ Новини по категорії """

    model = News
    template_name = 'news/index_page.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id']).title
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], 
            is_published=True)


class ViewNews(DetailView):
    """ Перегляд конкретної новини """

    model = News
    context_object_name = 'news_item'
    
class CreateNews(CreateView):
    """ Створення новини """

    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('news:index-page')