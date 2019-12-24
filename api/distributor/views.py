from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import TaskProcessedDataSerializer, TaskPathSerializer, TaskProcessedDataBoundingBoxSerializer , TaskPathBoundingBoxSerializer
from distributor.models import TaskPath, TaskProcessedData, TaskPathBoundingBox , TaskProcessedDataBoundingBox
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from distributor.distributor_system import DistributorSystem, DistributorSystemBoundingBox

import json

class getTask(APIView):
    """View for user task distribution that deals with images"""

    queryset = TaskPath.objects.all()
    permission_classes = [AllowAny]

    def get(self, request, pk):
        DS = DistributorSystem()
        TASK_TYPE = DS.TASK_TYPE
        if(DS.CURRENT_ITERATION == 0):
            DS.createPathIDSet()
            DS.createQueue()
            if(DS.DB_CREATED == False):
                DS.populateTaskPathModel()
                
        nextID = DS.get_next_ID(prevID = pk)
        if(nextID == None):
            return Response(status=status.HTTP_404_NOT_FOUND)

        taskpath = TaskPath.objects.get(taskgivenID = TASK_TYPE + str(nextID).zfill(6))
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


class getTaskBoundingBox(APIView):
    """View for user task distribution that deals with images"""

    queryset = TaskPathBoundingBox.objects.all()
    permission_classes = [AllowAny]

    def get(self, request, pk):
        DSBB = DistributorSystemBoundingBox()
        TASK_TYPE = DSBB.TASK_TYPE
        if(DSBB.CURRENT_ITERATION == 0):
            if(DSBB.DB_CREATED == False):
                DSBB.populateTaskPathBoundingBoxModel()
            # DSBB.createPathIDSet()
            DSBB.createQueue()
            

        nextID = DSBB.get_next_ID(prevID = pk)
        if(nextID == None):
            return Response(status=status.HTTP_404_NOT_FOUND)

        bb_taskpath = TaskPathBoundingBox.objects.get(bb_taskgivenID = TASK_TYPE + str(nextID).zfill(6))
        taskserialize = TaskPathBoundingBoxSerializer(bb_taskpath)
        DSBB.printQueue()
        return Response(taskserialize.data, status=status.HTTP_200_OK)

class postTaskBoundingBox(APIView):
    """View for user task distribution that deals with images"""

    queryset = TaskProcessedDataBoundingBox.objects.all()
    serializer_class = TaskProcessedDataBoundingBoxSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        print(request.data)
        print("\nposting\n")
        serializer = TaskProcessedDataBoundingBoxSerializer(data=request.data, context={'request': request})
        # print("outside serializer")
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
