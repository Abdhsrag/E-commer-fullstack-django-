from django.urls import path
from .views import (
    CategoryListView, CategoryCreateView, CategoryUpdateView,
    CategoryDeleteView, CategoryDetailView
)

urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),
    path('add/', CategoryCreateView.as_view(), name='category-add'),
    path('<int:pk>/edit/', CategoryUpdateView.as_view(), name='category-edit'),
    path('<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]