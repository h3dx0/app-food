from django.urls import path
from business import views
app_name = 'business'

urlpatterns = [
    path('', views.business_resume, name="business_resume"),
    path('category/add', views.category_add, name="category_add"),
    path('category/list', views.category_list, name="category_list"),
    path('product/list', views.product_list, name="product_list"),
    path('product/add', views.product_add, name="product_add"),
    path('order/list', views.order_list, name="order_list"),

]