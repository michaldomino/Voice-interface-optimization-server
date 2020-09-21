from rest_framework import serializers

from api import models


class TextKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TextKey
        fields = '__all__'


class TextLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TextLanguage
        fields = '__all__'


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Text
        fields = '__all__'


class TextResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TextResult
        fields = '__all__'
