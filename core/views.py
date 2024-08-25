from django.shortcuts import render, redirect

from core.models import Setting, Order, ServicePrice

# Create your views here.

def index(request):
    setting = Setting.objects.latest('id')
    services = ServicePrice.objects.all()
    context = {
        'setting':setting,
        'services':services
    }
    return render(request, 'index.html', context)

def add_req(request):
    phone = request.POST.get('phone')
    Order.objects.create(phone=phone)
    return redirect('index')
    