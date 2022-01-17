from rest_framework.pagination import PageNumberPagination


class UnitPagination(PageNumberPagination):
    page_size = 30
    max_page_size = 120
    page_query_description = "Номер страницы"
    page_size_query_param = "page_size"
    page_size_query_description = "Размер страницы"


class NutrientPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 60
    page_query_description = "Номер страницы"
    page_size_query_param = "page_size"
    page_size_query_description = "Размер страницы"


class ProductPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 30
    page_query_description = "Номер страницы"
    page_size_query_param = "page_size"
    page_size_query_description = "Размер страницы"
