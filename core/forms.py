from django import forms
from core.models import Order
from django.core.validators import RegexValidator

class OrderForm(forms.ModelForm):
    phone = forms.CharField(
        label='Телефон',
        max_length=15,
        min_length=7,
        validators=[
            RegexValidator(
                regex=r'^\+?[0-9]{1,4}?[-. \\\s]?[0-9]{1,3}?[-. \\\s]?[0-9]{1,4}?[-. \\\s]?[0-9]{1,9}$',
                message='Введите корректный номер телефона в формате: +123 456 7890',
            ),
        ],
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите номер телефона',
            'class': 'form-control',
            'aria-label': 'Телефон',
            'type':'tel',
        })
    )
    
    class Meta:
        model = Order
        fields = ('phone',)