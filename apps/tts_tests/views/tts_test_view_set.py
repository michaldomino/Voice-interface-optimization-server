from rest_framework import viewsets

from apps.tts_tests.models import TtsTest
from apps.tts_tests.serializers import TtsTestSerializer
from apps.users.permissions import IsVerified


class TtsTestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TtsTest.objects.all()
    serializer_class = TtsTestSerializer
    permission_classes = [IsVerified]
