from django.urls import path
from business import views
app_name = 'business'

urlpatterns = [
    path('', views.business_resume, name="business_resume"),
    path('category/add', views.category_add, name="category_add"),
    path('category/list', views.category_list, name="category_list"),
    path('menu/list', views.menu_list, name="menu_list"),
    path('menu/add', views.menu_add, name="menu_add"),
    path('order/list', views.order_list, name="order_list"),

]