from rest_framework import serializers
from distributor.models import TaskProcessedData, TaskPath
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

        print(validated_data)
        task = TaskPath.objects.get(taskgivenID = str(validated_data.get('taskpath')))
        task.taskCount = task.taskCount + 1
        task.save()
        
        return validated_data
