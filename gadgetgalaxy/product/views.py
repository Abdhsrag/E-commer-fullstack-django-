from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from category.models import Category
from django.views import View
from django.contrib.auth.decorators import login_required

# Create your views here.
class product_list_view(View):
    def get(self, request):
        products = Product.get_all_products()
        return render(request, 'products.html', {'products': products})
@login_required
def index(request):
    return render(request, 'index.html')

# def product_list(request):
#     products = Product.get_all_products()
#     return render(request, 'products.html', {'products': products})

from django.db import IntegrityError
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'product_success.html')
        else:
            categories = Category.get_all_categories()
            return render(request, 'add_products.html', {'form': form, 'categories': categories})
    else:
        form = ProductForm()
        categories = Category.get_all_categories()
        return render(request, 'add_products.html', {'form': form, 'categories': categories})

# def add_product(request):
#     if request.method == 'POST':
#         if request.POST['product_name'] and request.POST['product_desc'] and request.POST['product_price'] and request.POST['product_stock'] and request.POST['sku'] and request.POST['category'] and request.FILES['product_image'] is not None:
#             product_data = {
#                 'name': request.POST['product_name'],
#                 'description': request.POST['product_desc'],
#                 'price': request.POST['product_price'],
#                 'stock': request.POST['product_stock'],
#                 'image': request.FILES['product_image'],
#                 'sku': request.POST['sku'],
#                 'category_id': request.POST['category']
#             }
#             try:
#                 Product.create_product(**product_data)
#                 return render(request, 'product_success.html')
#             except IntegrityError:
#                 error_message = "Please use a unique SKU."
#                 categories = Category.get_all_categories()
#                 return render(request, 'add_products.html', {'categories': categories, 'error_message': error_message})
#         else:
#             error_message = "Please fill all the fields."
#             categories = Category.get_all_categories()
#             return render(request, 'add_products.html', {'categories': categories, 'error_message': error_message})
#     else:
#         categories = Category.get_all_categories()
#         return render(request, 'add_products.html', {'categories': categories})
@login_required
def page_not_found(request):
    return render(request, 'notfound.html', status=404)

@login_required
def success(request):
    return render(request, 'product_success.html')

@login_required
def hard_delete_product(request, product_id):
    if request.method == 'GET':
        Product.hard_delete_product(product_id)
        return render(request, 'product_success.html')
    else:
        return render(request, 'product_success.html')

class soft_delete_product(View):
    def get(self, request, product_id):
        Product.soft_delete_product(product_id)
        return render(request, 'product_success.html')

# def soft_delete_product(request, product_id):
#     if request.method == 'GET':
#         Product.soft_delete_product(product_id)
#         return render(request, 'product_success.html')
#     else:
#         return render(request, 'product_success.html')

@login_required
def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return render(request, 'product_success.html')
        else:
            return render(request, 'update_product.html', {'form': form, 'product': product})
    else:
        form = ProductForm(instance=product)
        return render(request, 'update_product.html', {'form': form, 'product': product})