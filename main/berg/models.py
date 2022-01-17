from django.db import models
from berg.managers import (
    UnitManager,
    NutrientManager,
    ProductManager,
    ProductStructManager,
)


class Nutrient(models.Model):
    nutrient_id = models.AutoField(primary_key=True)
    nutrient_name = models.CharField(max_length=150)
    status = models.IntegerField()

    class Meta:
        db_table = "nutrient"

    def __str__(self) -> str:
        return f"{self.nutrient_name}"

    nutrients = NutrientManager()


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=500)
    status = models.IntegerField()

    class Meta:
        db_table = "product"

    def __str__(self) -> str:
        return f"{self.product_name}"

    products = ProductManager()


class ProductJs(models.Model):
    product_js_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=500)
    product_js = models.TextField()  # This field type is a guess.
    source = models.CharField(max_length=150)

    class Meta:
        db_table = "product_js"


class ProductStruct(models.Model):
    product_struct_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    nutrient = models.ForeignKey(Nutrient, models.DO_NOTHING)
    unit = models.ForeignKey("Unit", models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    status = models.IntegerField()

    class Meta:
        db_table = "product_struct"

    def __str__(self) -> str:
        return f"{self.product} {self.nutrient} {self.quantity} {self.unit}"

    product_structs = ProductStructManager()


class Unit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    parent_id = models.IntegerField()
    parent_multiplier = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        db_table = "unit"

    def __str__(self) -> str:
        return f"{self.value}"

    units = UnitManager()
