from django.shortcuts import render, redirect
from django.http import HttpResponse
import qrcode
from django.utils.six import BytesIO


def index(request):
    if request.method == 'POST':
        data = request.POST.get('data', None)
        context = {'qr_data': data}
        return render(request, 'qr_code/qrcode.html', context)
    return render(request, 'qr_code/index.html')


def generate_qrcode(request, data):
    img = qrcode.make(data)
    buf = BytesIO()
    img.save(buf)
    image_stream = buf.getvalue()

    return HttpResponse(image_stream, content_type='image/png')

