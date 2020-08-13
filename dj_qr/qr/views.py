from django.shortcuts import render, HttpResponse
from segno import helpers

# Create your views here.


def index(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']

        qr = helpers.make_mecard(name, phone, email)
        qr.save('qr.png', scale=10)
        img = open('qr.png', 'rb').read()

        # return HttpResponse(f'数据提交: {name},{phone},{email}')
        return HttpResponse(img, content_type='image/png')
    return render(request, 'index.html')
