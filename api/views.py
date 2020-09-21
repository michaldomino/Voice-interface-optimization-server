from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from api import models, serializers


def _list_objects(model_class, serializer_class):
    objects = model_class.objects.all()
    serializer = serializer_class(objects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def keys_list(request):
    return _list_objects(models.TextKey, serializers.TextKeySerializer)


@api_view(['GET'])
def languages_list(request):
    return _list_objects(models.TextLanguage, serializers.TextLanguageSerializer)


@api_view(['GET'])
def text_list(request):
    return _list_objects(models.Text, serializers.TextSerializer)


@api_view(['GET'])
def text_result_list(request):
    return _list_objects(models.TextResult, serializers.TextResultSerializer)


@api_view(['POST'])
def text_create(request):
    serializer = serializers.TextSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def text_result_create(request):
    serializer = serializers.TextResultSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
