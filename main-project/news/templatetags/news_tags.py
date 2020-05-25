from django import template
from news.models import Category
from django.db.models import Count, F
from django.core.cache import cache


register = template.Library()

@register.simple_tag(name='get_list_categories')
def get_categories():

    # categories = cache.get('categories')
    # if not categories:
    categories = Category.objects.annotate(cnt=Count('get_news', filter=F('get_news__is_published'))).filter(cnt__gt=0)
    # cache.set('categories', categories, 30)
    return categories

@register.inclusion_tag('tags/list_categories.html')
def show_categories(arg1='hello', arg2='world'):
    categories = cache.get('categories')
    if not categories:
        categories = Category.objects.annotate(cnt=Count('get_news', filter=F('get_news__is_published'))).filter(cnt__gt=0)
        cache.set('categories', categories, 30)
    return {
        "categories": categories, 
        "arg1": arg1,
        "arg2": arg2,
    }