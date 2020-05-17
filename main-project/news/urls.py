from django.urls import path
from news import views


app_name = 'news'
urlpatterns = [
    path('', views.index_page, name='index-page'),
    path('category/<int:category_id>/', views.get_category, name='category'),
    path('<int:news_id>/', views.view_news, name='view-news'),
]