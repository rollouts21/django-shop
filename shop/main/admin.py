from django.contrib import admin
from .models import Product, Service, Category, About, Contacts


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_editable = []  # Убираем редактируемые поля, чтобы избежать конфликта
    list_display_links = ["name"]  # Указываем, что 'name' будет ссылкой


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ["name", "number", "second_number", "mail"]
    list_editable = [
        "number",
        "second_number",
        "mail",
    ]  # Убираем 'name' из редактируемых полей


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "price",
        "available",
        "created",
        "updated",
        "amount",
    ]
    list_filter = ["available", "created", "updated"]
    list_editable = ["price", "available", "amount"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "price", "available"]
    list_filter = ["available"]
    list_editable = ["price", "available"]  # Добавляем редактируемые поля
    prepopulated_fields = {"slug": ("name",)}
