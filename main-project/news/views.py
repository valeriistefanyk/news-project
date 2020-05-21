from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Category
from news.froms import NewsForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



from django.core.paginator import Paginator

def test(request):
    objects = ['john', 'valerii', 'some', 'something 4', 'something 5']
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)
    return render(request, 'news/test.html', {'page_obj': page_obj})


class HomeNews(ListView):
    """ Всі новини """

    model = News
    template_name = 'news/index_page.html'
    context_object_name = 'news'
    paginate_by = 10

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
    
class CreateNews(LoginRequiredMixin, CreateView):
    """ Створення новини """

    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('news:index-page')
    login_url = '/admin/'