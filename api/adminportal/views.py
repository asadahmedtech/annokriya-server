from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
# from .serializers import UserDashboardSerializer
from merger.models import BoundingBoxObject, BoundingBoxObjectnew
from distributor.models import TaskProcessedDataBoundingBox

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

import json

from .serializers import TaskListSerializer, CustomPagination, OutPointsSerializer

class TaskListCreateAPIView(ListCreateAPIView):

    serializer_class = TaskListSerializer
    pagination_class = CustomPagination
    queryset = BoundingBoxObjectnew.objects.all()

class OutPointsCreateAPIView(ListCreateAPIView):

	serializer_class = OutPointsSerializer
	pagination_class = CustomPagination
	queryset = TaskProcessedDataBoundingBox.objects.all()