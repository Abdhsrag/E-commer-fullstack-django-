from . import views
from django.urls import path, include
from product.api.views import product_list_api, ProductUpdateAPI, ProductGetIdUpdateDeleteAPI, ProductViewSet, SoftDeletedProductListAPI
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('API/', product_list_api, name='apiall'),
    path('API/<int:pk>/', ProductUpdateAPI.as_view(), name='apiupdate'),
    path('APG/<int:pk>/', ProductGetIdUpdateDeleteAPI.as_view(), name='apigetid'),
    path('', views.product_list_view.as_view(), name='product_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('notfound/', views.page_not_found, name='404'),
    path('success/', views.success, name='success'),
    path('hard_delete/<int:product_id>/', views.hard_delete_product, name='hard_delete_product'),
    path('soft_delete/<int:product_id>/', views.soft_delete_product.as_view(), name='soft_delete_product'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('API/soft_deleted/', SoftDeletedProductListAPI.as_view(), name='soft_deleted_products_api'),
path('soft_deleted/', views.soft_deleted_products_page, name='soft_deleted_products_page'),
    path('viewset/', include(router.urls)),
]