from django.urls import path, include

from rest_framework.routers import DefaultRouter
from apps.stt_tests import views

router = DefaultRouter()
router.register(r'stt_tests', views.SttTestViewSet)
router.register(r'xlsx', views.SttTestResultXlsxViewSet)
router.register(r'stt_test_results', views.CreateSttTestResultViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
