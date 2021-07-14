from rest_framework import serializers

from apps.stt_tests.models import SttTestResult


class SttTestResultXlsxSerializer(serializers.ModelSerializer):
    language = serializers.CharField(source='stt_test.language.code')
    text = serializers.CharField(source='stt_test.text')

    class Meta:
        model = SttTestResult
        fields = ['language', 'text', 'result']

    def get_formatted_result(self, obj):
        return int(obj.result)
