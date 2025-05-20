from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/')
    @classmethod
    def get_all_categories(cls):
        return cls.objects.all()

    def __str__(self):
        return self.name