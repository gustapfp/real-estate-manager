from rest_framework import authentication
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from structlog import get_logger

from real_state_manager.real_estate.api.serializers import PropertySerializer
from real_state_manager.real_estate.models import Property

logger = get_logger()


class PropertyView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """Get all properties for the authenticated user

        Args:
            request (_type): Request object

        Returns:
            _type_: Response object
        """
        try:
            properties = Property.objects.filter(user=request.user)  # pyright: ignore[reportAttributeAccessIssue]
            serializer = PropertySerializer(properties, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception("Unable to retrieve properties for user", error=e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        """Create a new property for the authenticated user

        Args:
            request (_type): Request object

        Returns:
            _type_: Response object
        """
        try:
            serializer = PropertySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            logger.error("Invalid data for property creation", errors=serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception("Unable to create property", error=e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ReservationView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
