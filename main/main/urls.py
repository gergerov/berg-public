from django.contrib import admin
from django.urls import path, include, re_path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions

from berg.routers import berg_router


schema_view = get_schema_view(
    openapi.Info(
        title="Состав продуктов",
        default_version="v1",
        description="Приложение состава продуктов",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="gergerov94@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

doc_urls = [
    re_path(
        "swagger(?P<format>\.json|\.yaml)",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(berg_router.urls)),
    path("api/v1/", include("berg.urls")),
    path("api/v1/account/", include("account.urls")),
] + doc_urls
