from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.authentication.serializers import IsVerifiedSerializer


class IsVerifiedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = IsVerifiedSerializer(request.user)
        return Response(serializer.data)
