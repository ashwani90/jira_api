from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'is_active']