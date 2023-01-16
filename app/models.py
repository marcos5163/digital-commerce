import email
from itertools import product
from locale import currency
from multiprocessing.spawn import old_main_modules
from ssl import OP_NO_RENEGOTIATION
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Seller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    phone = models.CharField(max_length=20)


class Country(models.Model):
    name = models.CharField(max_length=100)
    code_v2 = models.CharField(max_length=2)


class Currency(models.Model):
    name = models.CharField(max_length=100)
    currency_code = models.CharField(max_length=3)


class Address(models.Model):
    address_line_1 = models.CharField(max_length=100, blank=True, null=True)
    address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    Country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, blank=True
    )
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)


class Store(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    link = models.CharField(max_length=500)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    original_price = models.DecimalField(max_digits=19, decimal_places=10)
    selling_price = models.DecimalField(max_digits=19, decimal_places=10)
    cover_images = ArrayField(
        models.URLField(max_length=500, null=True, blank=True), size=5
    )
    link = models.CharField(max_length=500)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)
    discription = models.CharField(max_length=2000)


class ProductContent(models.Model):

    AUDIO = "AUDIO"
    VIDEO = "VIDEO"
    IMAGE = "IMAGE"
    DOC = "DOC"

    PRODUCT_CONTENT_TYPE_CHOICES = (
        (AUDIO, "AUDIO"),
        (VIDEO, "VIDEO"),
        (IMAGE, "IMAGE"),
        (DOC, "DOC"),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_content_type = models.CharField(
        max_length=100, choices=PRODUCT_CONTENT_TYPE_CHOICES
    )
    title = models.CharField(max_length=100)
    resource = models.URLField(max_length=1000)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    billing_address = models.ForeignKey(
        Address, blank=True, on_delete=models.SET_NULL, null=True
    )


class Sale(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)


class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product_id = models.PositiveIntegerField()
    selling_price = models.DecimalField(max_digits=19, decimal_places=10)
