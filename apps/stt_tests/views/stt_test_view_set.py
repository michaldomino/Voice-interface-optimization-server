from rest_framework import viewsets

from apps.stt_tests.models import SttTest
from apps.stt_tests.serializers import SttTestSerializer
from apps.users.permissions import IsVerified


class SttTestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SttTest.objects.all()
    serializer_class = SttTestSerializer
    permission_classes = [IsVerified]
