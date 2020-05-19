from django.urls import path
from news import views


app_name = 'news'
urlpatterns = [
    path('', views.HomeNews.as_view(), name='index-page'),
    path('category/<int:category_id>/', views.NewsByCategory.as_view(), name='category'),
    path('<int:pk>/', views.ViewNews.as_view(), name='view-news'),
    path('add/', views.CreateNews.as_view(), name='add-news'),
    # path('add/', views.add_news, name='add-news'),
]