from rest_framework import serializers

from apps.tts_tests.models import TtsTestResult


class TtsTestResultXlsxSerializer(serializers.ModelSerializer):
    language = serializers.CharField(source='tts_test.language.code')
    text = serializers.CharField(source='tts_test.text')
    volume = serializers.FloatField(source='tts_test.volume')
    pitch = serializers.FloatField(source='tts_test.pitch')
    rate = serializers.FloatField(source='tts_test.rate')
    words_count = serializers.SerializerMethodField()
    age = serializers.IntegerField(source='user.age')
    formatted_result = serializers.SerializerMethodField()

    class Meta:
        model = TtsTestResult
        fields = ['language', 'text', 'volume', 'pitch', 'rate', 'words_count', 'age', 'formatted_result']

    def get_words_count(self, obj):
        return len(obj.tts_test.text.split())

    def get_formatted_result(self, obj):
        return int(obj.result)
