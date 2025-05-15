from . import views
from django.urls import path
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('notfound/', views.page_not_found, name='404'),
    path('success/', views.success, name='success'),
]