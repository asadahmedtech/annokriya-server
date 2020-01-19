from rest_framework import serializers
from authentication.models import User, UserProfile
from merger.models import BoundingBoxObject, BoundingBoxObjectnew, BoundingBoxObjectall
from distributor.models import TaskProcessedDataBoundingBox

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'results': data
        })


class TaskListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BoundingBoxObjectnew
        fields = '__all__'

class OutPointsSerializer(serializers.ModelSerializer):

	class Meta:
		model = BoundingBoxObjectall
		fields = '__all__'