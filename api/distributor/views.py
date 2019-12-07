from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import TaskProcessedDataSerializer, TaskPathSerializer
from distributor.models import TaskPath, TaskProcessedData
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from distributor.distributor_system import DistributorSystem

import json

TASK_TYPE = 'IMGAA'

class getTask(APIView):
    """View for user task distribution that deals with images"""

    queryset = TaskPath.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        DS = DistributorSystem()
        if(DS.CURRENT_ITERATION == 0):
            DS.createPathIDSet()
            DS.createQueue()
            if(DS.DB_CREATED == False):
                DS.populateTaskPathModel()
                
        nextID = DS.get_next_ID(prevID = pk)
        if(nextID == None):
            return Response(status=status.HTTP_404_NOT_FOUND)

        taskpath = TaskPath.objects.get(taskgivenID = 'IMGAA' + str(nextID).zfill(6))
        taskserialize = TaskPathSerializer(taskpath)
        DS.printQueue()
        return Response(taskserialize.data, status=status.HTTP_200_OK)

class postTask(APIView):
    """View for user task distribution that deals with images"""

    queryset = TaskProcessedData.objects.all()
    serializer_class = TaskProcessedDataSerializer

    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = TaskProcessedDataSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
