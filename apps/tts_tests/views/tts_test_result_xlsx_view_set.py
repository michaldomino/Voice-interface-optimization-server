from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.tts_tests.models import TtsTestResult
from apps.tts_tests.serializers import TtsTestResultXlsxSerializer


class TtsTestResultXlsxViewSet(XLSXFileMixin, ReadOnlyModelViewSet):
    queryset = TtsTestResult.objects.all()
    serializer_class = TtsTestResultXlsxSerializer
    permission_classes = [IsAdminUser]
    renderer_classes = [XLSXRenderer]
    filename = 'tts_tests_results.xlsx'
