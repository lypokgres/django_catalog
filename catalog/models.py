from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)


class Subcategory(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)


class Good(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=20)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True)
