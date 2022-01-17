from rest_framework import serializers as s
from berg.models import Product, ProductStruct, Nutrient, Unit


class UnitSerializer(s.HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        fields = (
            "unit_id",
            "value",
            "url",
        )


class NutrientSerializer(s.HyperlinkedModelSerializer):
    class Meta:
        model = Nutrient
        fields = (
            "nutrient_id",
            "nutrient_name",
            "status",
            "url",
        )


class ProductSerializer(s.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = (
            "product_id",
            "product_name",
            "status",
            "url",
        )


class ProductStructSerializer(s.ModelSerializer):
    nutrient = NutrientSerializer()
    unit = UnitSerializer()

    class Meta:
        model = ProductStruct
        fields = (
            "product_struct_id",
            "nutrient",
            "quantity",
            "unit",
            "status",
        )


class ProductStructShortSerializer(s.Serializer):
    nutrient = s.CharField(source="nutrient__nutrient_name")
    quantity = s.DecimalField(max_digits=10, decimal_places=3)
    unit = s.CharField(source="unit__value")


class TopProductByNutrientSerializer(s.Serializer):
    product = s.CharField(source="product__product_name")
    nutrient = s.CharField(source="nutrient__nutrient_name")
    quantity = s.DecimalField(max_digits=10, decimal_places=3)
    unit = s.CharField(source="unit__value")
