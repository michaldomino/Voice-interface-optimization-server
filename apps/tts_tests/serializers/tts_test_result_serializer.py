from rest_framework import serializers

from apps.tts_tests.models import TtsTestResult


class TtsTestResultSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = TtsTestResult
        fields = '__all__'
