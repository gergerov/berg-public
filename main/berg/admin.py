from django.contrib import admin
from django.contrib.admin.decorators import register
from berg.models import Nutrient, Product, ProductStruct, Unit


@register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = (
        "unit_id",
        "value",
    )


@register(Nutrient)
class NutrientAdmin(admin.ModelAdmin):
    list_display = (
        "nutrient_id",
        "nutrient_name",
        "status",
    )
    list_filter = ("status",)


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_id",
        "product_name",
        "status",
    )
    list_filter = ("status",)


@register(ProductStruct)
class ProductStructAdmin(admin.ModelAdmin):
    list_display = (
        "product_struct_id",
        "product",
        "nutrient",
        "quantity",
        "unit",
        "status",
    )
    list_filter = ("status",)
    search_fields = ("product__product_name",)
