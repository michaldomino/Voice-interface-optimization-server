from rest_framework import viewsets, mixins

from apps.tts_tests.models import TtsTestResult
from apps.tts_tests.serializers import TtsTestResultSerializer
from apps.users.permissions import IsVerified


class CreateTtsTestResultViewSet(mixins.CreateModelMixin,
                                 viewsets.GenericViewSet):
    queryset = TtsTestResult.objects.all()
    serializer_class = TtsTestResultSerializer
    permission_classes = [IsVerified]
