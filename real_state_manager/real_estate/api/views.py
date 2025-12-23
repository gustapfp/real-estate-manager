from rest_framework import authentication
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from real_state_manager.real_estate.api.serializers import PropertySerializer
from real_state_manager.real_estate.models import Property


class PropertyView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        properties = Property.objects.filter(user=request.user)  # pyright: ignore[reportAttributeAccessIssue]
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)
