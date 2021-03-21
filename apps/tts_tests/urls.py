from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.tts_tests import views

router = DefaultRouter()
router.register(r'tts_tests', viewset=views.TtsTestViewSet)
router.register(r'tts_test_results', viewset=views.CreateTtsTestResultViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
