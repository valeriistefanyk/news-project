from django.shortcuts import render
from testapp.models import Rubric

def test(request):
    context = {}
    context['rubrics'] = Rubric.objects.all()
    return render(request, 'testapp/test.html', context)


def get_rubric(request):
    pass