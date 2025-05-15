from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    sku = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    @classmethod
    def get_all_products(cls):
        return cls.objects.filter(is_deleted=False)

    @classmethod
    def get_products_by_category(cls, category_id):
        return cls.objects.filter(category_id=category_id)

    @classmethod
    def create_product(cls, **arg):
        return cls.objects.create(**arg)

    @classmethod
    def hard_delete_product(cls, product_id):
        product = cls.objects.get(id=product_id)
        product.delete()

    @classmethod
    def soft_delete_product(cls, product_id):
        product = cls.objects.get(id=product_id)
        product.is_deleted = True
        product.save()
