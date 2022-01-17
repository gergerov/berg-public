from django.urls import path
from berg.views import ProductStructView, ProductStructShortView, TopProductByNutrient

urlpatterns = [
    path(
        "product_struct_by_product/<int:product_id>",
        view=ProductStructView.as_view(),
        name="product-struct-by-product",
    ),
    path(
        "product_struct_by_product/<int:product_id>/short",
        view=ProductStructShortView.as_view(),
        name="product-struct-by-product-short",
    ),
    path(
        "top_product_by_nutrient/<int:nutrient_id>/<int:nums>",
        view=TopProductByNutrient.as_view(),
        name="top-product-by-nutrient",
    ),
]
