from django.urls import re_path, path
from .views import index, generate_qrcode


app_name = 'qr_code'
urlpatterns = [
    path('', index, name='index'),
    path('<str:data>', generate_qrcode, name='qrcode'),
]