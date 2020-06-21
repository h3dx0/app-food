from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.
from business.forms import ProductForm
from business.models import Order, Product


def business_resume(request):
    return render(request, 'business_resume.html')


def category_add(request):
    return render(request, 'category/add_category.html')


def category_list(request):
    return render(request, 'category/list_category.html')


def product_list(request):
    products = Product.objects.all().order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(products, 20)
    products_paginated = paginator.get_page(page)

    context = {'products': products_paginated}
    return render(request, 'product/list_product.html', context=context)


def product_add(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/negocio/product/list')
    context = {
        'form': form
    }
    return render(request, 'product/add_product.html', context=context)


def order_list(request):
    orders = Order.objects.all().order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(orders, 20)
    orders_paginated = paginator.get_page(page)

    context = {'orders': orders_paginated}
    return render(request, 'orders/list_orders.html', context=context)
