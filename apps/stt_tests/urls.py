from django.urls import path

from apps.stt_tests.views.stt_test_view_set import SttTestViewSet

urlpatterns = [
    path('api/stt_test', SttTestViewSet.as_view({'get': 'list'})),
]
