from django.shortcuts import render, redirect
from .models import Orders, Products, Customers
from .forms import OrderForm


def index(request):
    orders_all = Orders.objects.all()
    return render(request, 'myapp/index.html', {'orders_all': orders_all})


def order_form(request):
    error = ''
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = OrderForm()
    context = {'form': form, 'error': error}
    return render(request, 'myapp/order_form.html', context)
