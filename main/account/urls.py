from django.urls import path
from account.views import RegistrationView, GetAuthToken


urlpatterns = [
    path("registration", view=RegistrationView.as_view(), name="registration"),
    path("get_token", GetAuthToken.as_view(), name="get-token"),
]
