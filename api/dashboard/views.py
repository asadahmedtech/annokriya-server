from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import UserDashboardSerializer
from dashboard.models import Dashboard

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

import json

class UserDashboard(APIView):
    """View for user to update their profile"""

    queryset = Dashboard.objects.all()
    serializer_class = UserDashboardSerializer

    permission_classes = [IsAuthenticated]

    def get(self, request):
        # user = UserProfile.objects.get(pk= pk)
        

        dashboard = Dashboard.objects.get(user=request.user)
        serializer = UserDashboardSerializer(dashboard)
        print("==> DashBoard : ", request.user)
        print("==> Dashboard : ", serializer.data)

        temp_data = {"pending": str(dashboard.pending), "correct": str(dashboard.correct), "wrong": str(dashboard.wrong), "credits": str(dashboard.credits)}
        temp_data = json.dumps(temp_data)
        print(temp_data)
        return Response(serializer.data, status=status.HTTP_200_OK)

