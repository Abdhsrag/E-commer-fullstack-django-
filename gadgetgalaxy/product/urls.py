from . import views
from django.urls import path
urlpatterns = [
    path('', views.product_list_view.as_view(), name='product_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('notfound/', views.page_not_found, name='404'),
    path('success/', views.success, name='success'),
    path('hard_delete/<int:product_id>/', views.hard_delete_product, name='hard_delete_product'),
    path('soft_delete/<int:product_id>/', views.soft_delete_product, name='soft_delete_product'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
]