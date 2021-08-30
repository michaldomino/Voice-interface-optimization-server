from rest_framework import serializers

from apps.stt_tests.models import SttTestResult


class SttTestResultSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = SttTestResult
        fields = '__all__'
