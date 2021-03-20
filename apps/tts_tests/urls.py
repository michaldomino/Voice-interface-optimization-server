from django.urls import path

from apps.tts_tests.views import TtsTestViewSet

urlpatterns = [
    path('api/tts_test', TtsTestViewSet.as_view({'get': 'list'})),
]
