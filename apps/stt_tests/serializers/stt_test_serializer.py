from rest_framework import serializers

from apps.stt_tests.models import SttTest


class SttTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SttTest
        fields = '__all__'
