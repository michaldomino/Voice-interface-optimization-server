from django.urls import path

from api import views

urlpatterns = [
    path('key-list', views.keys_list, name='key-list'),
    path('lang-list', views.languages_list, name='lang-list'),
    path('text-list', views.text_list, name='text-list'),
    path('tr-list', views.text_result_list, name='tr-list'),
    path('text-create', views.text_create, name='text-create'),
    path('tr-create', views.text_result_create, name='tr-create'),
]
