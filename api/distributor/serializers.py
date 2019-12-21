from rest_framework import serializers
from distributor.models import TaskProcessedData, TaskPath, TaskPathBoundingBox , TaskProcessedDataBoundingBox
from dashboard.models import Dashboard
from django.db.models import F

class TaskPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskPath
        fields = '__all__'


class TaskProcessedDataSerializer(serializers.ModelSerializer):
    # TaskPath = TaskPathSerializer(required = True)
    class Meta:
        model = TaskProcessedData
        fields = ('taskpath', 'x1', 'x2', 'x3', 'x4', 'x5', 'y1', 'y2', 'y3', 'y4', 'y5')

    def create(self, validated_data):
        user = self.context['request'].user
        TaskProcessedData.objects.create(user=user, **validated_data)

        dashboard_obj = Dashboard.objects.get(user=user)
        dashboard_obj.pending = dashboard_obj.pending + 1
        dashboard_obj.save()
        
        print(validated_data)
        task = TaskPath.objects.get(taskgivenID = str(validated_data.get('taskpath')))
        task.taskCount = task.taskCount + 1
        task.save()
        
        return validated_data



class TaskPathBoundingBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskPathBoundingBox
        fields = '__all__'


class SingleTaskPathBoundingBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskProcessedDataBoundingBox
        fields = ('bb_taskpath', 'x', 'y', 'l', 'h')


class TaskProcessedDataBoundingBoxSerializer(serializers.ModelSerializer):
    # TaskPath = TaskPathSerializer(required = True)
    # print("in serializer")
    multipleBoundingBox = SingleTaskPathBoundingBoxSerializer(many=True)
    # def __init__(self, *args, **kwargs):
    #     many = kwargs.pop('many', True)
    #     super(TaskProcessedDataBoundingBoxSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = TaskProcessedDataBoundingBox
        fields=('bb_taskpath', 'multipleBoundingBox')

    def create(self, validated_data):
        user = self.context['request'].user
        print(user)
        # TaskProcessedDataBoundingBox.objects.create(user=user, **validated_data)
        multipleBoundingBox_data=validated_data.pop('multipleBoundingBox')
        for d in multipleBoundingBox_data:
            TaskProcessedDataBoundingBox.objects.create(user=user, **d)
            # print(**d)
        dashboard_obj = Dashboard.objects.get(user=user)
        dashboard_obj.pending = dashboard_obj.pending + 1
        dashboard_obj.save()

        print(validated_data)
        task = TaskPathBoundingBox.objects.get(bb_taskgivenID = str(validated_data.get('bb_taskpath')))
        task.bb_taskCount = task.bb_taskCount + 1
        task.save()

        return validated_data
