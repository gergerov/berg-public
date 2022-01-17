from rest_framework import serializers as s
from django.contrib.auth.models import User


class RegistrationUserSerializer(s.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "email",
        )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        # если вернуть объект пользователя, то в api вернет хэшированный пароль
        return validated_data
