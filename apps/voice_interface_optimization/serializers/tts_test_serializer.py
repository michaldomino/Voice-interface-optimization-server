from rest_framework import serializers

from apps.voice_interface_optimization.models import TtsTest


class TtsTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = TtsTest
        fields = '__all__'