from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.stt_tests.models import SttTestResult
from apps.stt_tests.serializers import SttTestResultXlsxSerializer


class SttTestResultXlsxViewSet(XLSXFileMixin, ReadOnlyModelViewSet):
    queryset = SttTestResult.objects.all()
    serializer_class = SttTestResultXlsxSerializer
    permission_classes = [IsAdminUser]
    renderer_classes = [XLSXRenderer]
    filename = 'stt_tests_results.xlsx'
