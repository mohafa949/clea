from django.contrib import admin

# Register your models here.

from .models import Product, News, Partner

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("name",)