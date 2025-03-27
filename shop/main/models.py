from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ("name",)
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    amount = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "продукт"
        verbose_name_plural = "продукты"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("main:product_detail", args=[self.slug])


class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "услуга"
        verbose_name_plural = "услуги"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("main:service_detail", args=[self.slug])


class About(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "о нас"
        verbose_name_plural = "о нас"

    def __str__(self):
        return self.name


class Contacts(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    second_number = models.CharField(max_length=200, blank=True)
    mail = models.CharField(max_length=200)

    class Meta:
        verbose_name = "контакты"
        verbose_name_plural = "контакты"

    def __str__(self):
        return self.name
