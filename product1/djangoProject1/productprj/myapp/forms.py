from .models import Orders, Products, Customers
from django.forms import ModelForm, TextInput, Select, DateInput, NumberInput


class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = ["order_number", "order_date", "prod", "cust", "quantity", "price"]
        widgets = {
            "order_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер',
                'required': True
            }),
            "order_date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата заказа',
                'required': True
            }),
            "prod": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Товар',
                'required': True
            }),
            "cust": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Клиент',
                'required': True
            }),
            "quantity": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество',
                'required': True
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена',
                'required': True
            })
        }