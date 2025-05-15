from django.shortcuts import render
from .models import Product
from category.models import Category

# Create your views here.
def index(request):
    return render(request, 'index.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        stock = request.POST['stock']
        image = request.FILES['image']
        sku = request.POST['sku']
        category = request.POST['category']
        product = Product(
            name=name,
            description=description,
            price=price,
            stock=stock,
            image=image,
            sku=sku,
            category_id=category
        )
        product.save()
        return render(request, 'product_success.html', {'product': product})
    else:
        categories = Category.objects.all()
        return render(request, 'add_products.html', {'categories': categories})


def page_not_found(request):
    return render(request, 'notfound.html', status=404)

def success(request):
    return render(request, 'product_success.html')