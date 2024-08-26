from django import template 
from core.forms import OrderForm
from core.models import *

register = template.Library()


@register.inclusion_tag('components/sections/about.html')
def about():
    section = Section.objects.get(section='Информация')
    album = Album.objects.all()
    context = {
        'section':section,
        'album':album,
    }
    return context

@register.inclusion_tag('components/sections/services.html')
def services():
    section = Section.objects.get(section='Услуги')
    context = {
        'section':section
    }
    return context

@register.inclusion_tag('components/sections/banner.html')
def banner():
    section = Section.objects.get(section='Баннер')
    form = OrderForm()
    context = {
        'section':section,
        'form':form,
        
    }
    return context

