from django.shortcuts import render


def index_page(request):
    """ Стартовая страница """

    context = {}
    return render(request, 'news/index_page.html', context)