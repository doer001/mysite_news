from django.urls import path
from news import views


app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('column/<slug:column_slug>/', views.column_detail, name='column'),
    path('article/<int:pk>/', views.article_detail, name='article'),
]
