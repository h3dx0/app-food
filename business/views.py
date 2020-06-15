from django.shortcuts import render


# Create your views here.
def business_resume(request):
    return render(request, 'business_resume.html')


def category_add(request):
    return render(request, 'category/add_category.html')


def category_list(request):
    return render(request, 'category/list_category.html')


def product_list(request):
    return render(request, 'product/list_product.html')


def product_add(request):
    return render(request, 'product/add_product.html')


def order_list(request):
    return render(request, 'orders/list_orders.html')
