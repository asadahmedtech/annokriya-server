from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import UserDashboardSerializer
from dashboard.models import Dashboard

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

class UserDashboard(APIView):
    """View for user to update their profile"""

    queryset = Dashboard.objects.all()
    serializer_class = UserDashboardSerializer

    permission_classes = [IsAuthenticated]

    def get(self, request):
        # user = UserProfile.objects.get(pk= pk)
        serializer = UserDashboardSerializer(request.user, context={'request': request})
        return Response(serializer.data)

