from rest_framework import serializers

from apps.tts_tests.models import TtsTest


class TtsTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TtsTest
        fields = '__all__'
