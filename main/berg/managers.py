from django.db import models


class UnitManager(models.Manager):
    def all(self):
        return self.get_queryset().order_by("unit_id")


class NutrientManager(models.Manager):
    def all(self):
        return self.get_queryset().order_by("nutrient_name")

    def active(self):
        return self.all().filter(status=0)


class ProductManager(models.Manager):
    def all(self):
        return self.get_queryset().order_by("product_name")

    def active(self):
        return self.all().filter(status=0)


class ProductStructQuerySet(models.QuerySet):
    def active(self):
        """Только активные составы"""
        return self.filter(status=0)

    def by_product(self, product_id):
        """Состав продукта по продукту"""
        return self.filter(product__product_id=product_id)

    def related(self):
        """Все нужные связи"""
        return self.select_related("unit", "product", "nutrient")

    def ordered(self):
        """Сортировка по product_struct_id asc"""
        return self.order_by("product_struct_id")

    def by_nutrient(self, nutrient_id):
        """Составы по нутриенту"""
        return self.filter(nutrient__nutrient_id=nutrient_id)

    def order_by_quantity(self):
        """Сортировка по убыванию количества в составе"""
        return self.order_by("-quantity")

    def top(self, nums: int):
        """Первые nums записей"""
        return self[0:nums]


class ProductStructManager(models.Manager):
    def get_queryset(self):
        return ProductStructQuerySet(self.model, self._db)

    def all(self):
        """Все записи отсортированные по id"""
        return self.get_queryset().ordered()

    def by_product(self, product_id):
        """Состав определенного продукта, отсортированный по id с нужными связями"""
        return self.get_queryset().ordered().related().by_product(product_id)

    def by_nutrient_quantity(self, nutrient_id, nums):
        return (
            self.get_queryset()
            .active()
            .related()
            .by_nutrient(nutrient_id)
            .order_by_quantity()
            .top(nums)
        )
