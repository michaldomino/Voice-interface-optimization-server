from rest_framework import serializers

from apps.stt_tests.models import SttTestResult


class SttTestResultXlsxSerializer(serializers.ModelSerializer):
    language = serializers.CharField(source='stt_test.language.code')
    text = serializers.SerializerMethodField()
    formatted_result = serializers.SerializerMethodField()

    class Meta:
        model = SttTestResult
        fields = ['language', 'text', 'result', 'formatted_result']

    def get_text(self, obj):
        return obj.stt_test.text.lower()

    def get_formatted_result(self, obj):
        return obj.result.lower()
