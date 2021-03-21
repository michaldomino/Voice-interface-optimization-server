from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

UserModel = get_user_model()


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    def create(self, validated_data):
        user = UserModel.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password',)
