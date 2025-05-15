from django.shortcuts import render
from .models import Product
from category.models import Category

# Create your views here.
def index(request):
    return render(request, 'index.html')

def product_list(request):
    products = Product.get_all_products()
    return render(request, 'products.html', {'products': products})

from django.db import IntegrityError

def add_product(request):
    if request.method == 'POST':
        if request.POST['product_name'] and request.POST['product_desc'] and request.POST['product_price'] and request.POST['product_stock'] and request.POST['sku'] and request.POST['category'] and request.FILES['product_image'] is not None:
            product_data = {
                'name': request.POST['product_name'],
                'description': request.POST['product_desc'],
                'price': request.POST['product_price'],
                'stock': request.POST['product_stock'],
                'image': request.FILES['product_image'],
                'sku': request.POST['sku'],
                'category_id': request.POST['category']
            }
            try:
                Product.create_product(**product_data)
                return render(request, 'product_success.html')
            except IntegrityError:
                error_message = "Please use a unique SKU."
                categories = Category.get_all_categories()
                return render(request, 'add_products.html', {'categories': categories, 'error_message': error_message})
        else:
            error_message = "Please fill all the fields."
            categories = Category.get_all_categories()
            return render(request, 'add_products.html', {'categories': categories, 'error_message': error_message})
    else:
        categories = Category.get_all_categories()
        return render(request, 'add_products.html', {'categories': categories})

def page_not_found(request):
    return render(request, 'notfound.html', status=404)

def success(request):
    return render(request, 'product_success.html')