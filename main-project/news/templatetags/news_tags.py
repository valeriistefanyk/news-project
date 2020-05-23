from django import template
from news.models import Category
from django.db.models import Count, F

register = template.Library()

@register.simple_tag(name='get_list_categories')
def get_categories():

    categories = Category.objects.annotate(cnt=Count('get_news', filter=F('get_news__is_published'))).filter(cnt__gt=0)
    return categories

@register.inclusion_tag('tags/list_categories.html')
def show_categories(arg1='hello', arg2='world'):
    
    categories = Category.objects.annotate(cnt=Count('get_news', filter=F('get_news__is_published'))).filter(cnt__gt=0)
    return {
        "categories": categories, 
        "arg1": arg1,
        "arg2": arg2,
    }