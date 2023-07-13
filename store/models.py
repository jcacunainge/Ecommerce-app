from django.db import models
from category.models import Category

# Create your models here.

class Product(models.Model):
    # Campo para el nombre del producto
    product_name = models.CharField(max_length=200, unique=True)

    # Campo para el slug del producto
    slug = models.CharField(max_length=200, unique=True)

    # Campo para la descripción del producto
    description = models.CharField(max_length=500, blank=True)

    # Campo para el precio del producto
    price = models.IntegerField()

    # Campo para las imágenes del producto
    images = models.ImageField(upload_to='photo/products')

    # Campo para el stock del producto
    stock = models.IntegerField()

    # Campo para indicar si el producto está disponible
    is_available = models.BooleanField(default=True)

    # Relación de muchos a uno con la categoría del producto
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # Campo para la fecha de creación del producto (se actualiza automáticamente)
    created_date = models.DateTimeField(auto_now=True)

    # Campo para la fecha de modificación del producto (se actualiza automáticamente)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name