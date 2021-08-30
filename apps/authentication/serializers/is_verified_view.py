from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class IsVerifiedSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['is_verified']
