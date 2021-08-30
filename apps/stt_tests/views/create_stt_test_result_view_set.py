from rest_framework import viewsets, mixins

from apps.stt_tests.models import SttTestResult
from apps.stt_tests.serializers import SttTestResultSerializer
from apps.users.permissions import IsVerified
from shared.mixins import CreateListModelMixin


class CreateSttTestResultViewSet(mixins.CreateModelMixin,
                                 CreateListModelMixin,
                                 viewsets.GenericViewSet):
    queryset = SttTestResult.objects.all()
    serializer_class = SttTestResultSerializer
    permission_classes = [IsVerified]
