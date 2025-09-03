from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=150)
    price = models.IntegerField(default=0)
    offer_price = models.FloatField(default=0)
    offer_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name