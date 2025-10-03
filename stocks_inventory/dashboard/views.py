from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm, OrderForm
from django.contrib import messages
# Create your views here.

@login_required
def index(request):
    orders= Order.objects.all()
    products= Product.objects.all()
    if request.method == 'POST':
        form= OrderForm(request.POST)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.staff= request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form= OrderForm()
    context = {
        'orders': orders,
        'form': form,
        'products': products,
    }
    return render(request, 'dashboard/index.html')

@login_required
def staff(request):
    workers= User.objects.all()
    workers_count= workers.count()
    orders_count= Order.objects.all().count()
    product_count= Products.objects.all().count()
    context= {
        'workers': workers,
        'workers_count' : workers_count,
        'orders_count': orders_count, 
        'product_count': products_count,
    }
    return render(request, 'dashboard/staff.html')

@login_required
def staff_detail(request, pk):
    workers= User.objects.get(id=pk)
    context= {
        'workers': worker,
    }
    return render(request, 'dashboard/staff_detail', context)

@login_required
def product(request):
    items= Product.objects.all() #using ORM
    #items= Product.objects.raw('SELECT * FROM dashboard_product')
    workers_count= User.objects.all().count()
    if request.method == 'POST':
        form= ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name= form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form= ProductForm()
    context= {
        'items': items,
        'form': form,
        'workers_count': workers_count,
    }
    return render(request, 'dashboard/product.html')

@login_required
def product_delete(request, pk):
    item= Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete')
    return render(request, 'dashboard/product_delete')

def product_update(request, pk):
    item= Product.objects.get(id= pk)
    if request.method== 'POST':
        form = ProductForm(request.POST, instance= item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form= ProductForm(instance= item)
    context= {
        'form': form
    }

@login_required
def order(request):
    orders= Order.objects.all()
    orders_count= orders.count()
    workers_count= User.objects.all().count()
    context= {
        'orders': orders,
        'workers_count': workers_count,
        'orders_count': orders_count,
    }
    return render(request, 'dashboard/order.html')

