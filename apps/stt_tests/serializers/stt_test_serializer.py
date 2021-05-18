from rest_framework import serializers

from apps.stt_tests.models import SttTest


class SttTestSerializer(serializers.ModelSerializer):
    text = serializers.SlugRelatedField(
        read_only=True,
        slug_field='text'
    )
    language = serializers.CharField(
        source='text.language.code'
    )

    class Meta:
        model = SttTest
        fields = '__all__'
