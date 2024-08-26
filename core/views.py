from django.shortcuts import render, redirect

from core.forms import OrderForm
from core.models import Setting, Order, ServicePrice, Contact
from django.core.mail import send_mail
# Create your views here.

def index(request):
    setting = Setting.objects.latest('id')
    services = ServicePrice.objects.all()
    contacts = Contact.objects.all()
    context = {
        'setting':setting,
        'services':services,
        'contacts':contacts,
    }
    return render(request, 'index.html', context)

def add_req(request):
    context = {}
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            setting = Setting.objects.latest('id')
            send_mail(
                'Пришла заявка',
                f"Пришла заявка. Номер телефона {form.cleaned_data['phone']}",
                'noreply@somehost.local',
                (setting.email, ),
                )
        else:
            context['errors'] = form.errors
    
    return render(request, 'respon.html', context)

'oaid wgwd doxk lbhw '