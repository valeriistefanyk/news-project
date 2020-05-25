from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Category
from news.forms import NewsForm, ContactForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.contrib import messages

from django.core.paginator import Paginator

def contact(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(
                form.cleaned_data['subject'],
                form.cleaned_data['content']
            )
            mail = send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['content'],
                'valeriistefanyk@ukr.net',
                ['valeriistefanyk@gmail.com'],
                fail_silently=True
            )
            if mail:
                messages.success(request, 'Успішно відправлено :)')
                return redirect('news:index-page')
            else:
                messages.error(request, 'Помилка відправки :(')
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'news/contact.html', context)


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
        return News.objects.filter(is_published=True).prefetch_related('category')


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