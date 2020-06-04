from django.urls import path
from testapp import views

app_name = 'testapp'
urlpatterns = [
    path('', views.test, name='test'),
    path('rubric/<int:pk>/', views.get_rubric, name='rubric'),
]