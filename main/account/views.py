from rest_framework.viewsets import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.throttling import ScopedRateThrottle
from account.serializers import RegistrationUserSerializer


class RegistrationView(generics.CreateAPIView):
    """Представление для регистрации пользователей"""

    serializer_class = RegistrationUserSerializer
    throttle_scope = "registration"


class GetAuthToken(ObtainAuthToken):
    """Представление для получения токена"""

    throttle_scope = "get-token"
    throttle_classes = [ScopedRateThrottle]
