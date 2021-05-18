from rest_framework import serializers

from apps.tts_tests.models import TtsTest


class TtsTestSerializer(serializers.ModelSerializer):
    text = serializers.SlugRelatedField(
        read_only=True,
        slug_field='text'
    )
    language = serializers.CharField(
        source='text.language.code'
    )

    class Meta:
        model = TtsTest
        fields = '__all__'