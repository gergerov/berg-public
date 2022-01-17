from rest_framework.viewsets import ModelViewSet, generics
from rest_framework.authentication import (
    TokenAuthentication,
    BasicAuthentication,
    SessionAuthentication,
)
from rest_framework.response import Response
from berg.serializers import (
    UnitSerializer,
    NutrientSerializer,
    ProductSerializer,
    ProductStructSerializer,
    ProductStructShortSerializer,
    TopProductByNutrientSerializer,
)
from berg.models import Unit, Nutrient, Product, ProductStruct
from berg.paginations import UnitPagination, NutrientPagination, ProductPagination
from berg.filters import ProductFilter
from berg.permissions import BergModelPermission


class BergModelViewSet(ModelViewSet):
    """
    Базовый класс modelvieset приложения berg.
    Задает права к представлению и методы аутентификации.
    Распределяет тротлинг в зависимости от категории пользователя
    (админу - одно, простому юзеру - другое)
    с помощью метода dispath.
    """

    authentication_classes = [
        TokenAuthentication,
        BasicAuthentication,
        SessionAuthentication,
    ]
    permission_classes = [BergModelPermission]

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.throttle_scope = "berg-admin"
        else:
            self.throttle_scope = "berg-user"
        return super().dispatch(request, *args, **kwargs)


class BergRetrieveAPIView(generics.RetrieveAPIView):
    """
    Базовый класс RetriveAPIView приложения Berg
    Задает права к представлению и методы аутентификации.
    Распределяет тротлинг в зависимости от категории пользователя
    (админу - одно, простому юзеру - другое)
    с помощью метода dispath.
    """

    authentication_classes = [
        TokenAuthentication,
        BasicAuthentication,
        SessionAuthentication,
    ]
    permission_classes = [BergModelPermission]

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.throttle_scope = "berg-admin"
        else:
            self.throttle_scope = "berg-user"
        return super().dispatch(request, *args, **kwargs)


class UnitViewSet(BergModelViewSet):
    """Представление единиц измерения"""

    serializer_class = UnitSerializer
    queryset = Unit.units.all()
    pagination_class = UnitPagination


class NutrientViewSet(BergModelViewSet):
    """Представление нутриентов"""

    serializer_class = NutrientSerializer
    queryset = Nutrient.nutrients.all()
    pagination_class = NutrientPagination


class ProductViewSet(BergModelViewSet):
    """Представление продуктов. Search - поиск по названию."""

    serializer_class = ProductSerializer
    queryset = Product.products.all()
    pagination_class = ProductPagination
    filter_backends = [ProductFilter]
    search_fields = [
        "^product_name",
    ]


class ProductStructView(BergRetrieveAPIView):
    """Представление состава продукта"""

    serializer_class = ProductStructSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data, status=200)

    def get_queryset(self):
        return ProductStruct.product_structs.by_product(self.kwargs["product_id"])


class ProductStructShortView(BergRetrieveAPIView):
    """Представление состава продукта (краткий формат)"""

    serializer_class = ProductStructShortSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        if len(queryset) == 0:
            return Response(status=404)
        return Response(serializer.data, status=200)

    def get_queryset(self):
        return ProductStruct.product_structs.by_product(
            self.kwargs["product_id"]
        ).values("nutrient__nutrient_name", "quantity", "unit__value")


class TopProductByNutrient(BergRetrieveAPIView):
    """
    Представления отражающее топ
    продуктов содержащих тот или иной нутриент
    """

    serializer_class = TopProductByNutrientSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset().values(
            "nutrient__nutrient_name",
            "quantity",
            "unit__value",
            "product__product_name",
        )

        serializer = self.serializer_class(queryset, many=True)
        if len(queryset) == 0:
            return Response(status=404)
        return Response(serializer.data, status=200)

    def get_queryset(self):
        return ProductStruct.product_structs.by_nutrient_quantity(
            nutrient_id=self.kwargs["nutrient_id"], nums=self.kwargs["nums"]
        )
