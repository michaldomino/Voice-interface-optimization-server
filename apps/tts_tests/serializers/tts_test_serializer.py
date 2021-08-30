from rest_framework import serializers

from apps.tts_tests.models import TtsTest


class TtsTestSerializer(serializers.ModelSerializer):
    language = serializers.CharField(
        source='language.code'
    )

    class Meta:
        model = TtsTest
        fields = '__all__'
