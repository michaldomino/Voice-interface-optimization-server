from rest_framework import viewsets

from apps.voice_interface_optimization.models import TtsTest
from apps.voice_interface_optimization.serializers import TtsTestSerializer


class TtsTestViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = TtsTest.objects.all()
    serializer_class = TtsTestSerializer