from django.urls import path
from .views import index, login, register, logout, hello

app_name = 'logins'
urlpatterns = [
    path('', hello),
    path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]
