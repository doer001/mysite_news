from django.urls import path
from . import views as blog_view


app_name = 'blog'
urlpatterns = [
    path('', blog_view.Index.as_view(), name='index'),
    path('search/', blog_view.Search.as_view(), name='search'),
    path('comment/', blog_view.pub_comment, name='comment'),
    path('category/<int:category>', blog_view.CategoryList.as_view(), name='category'),
    path('detail/<int:pk>', blog_view.ArticleDetail.as_view(), name='detail'),
]
