from rest_framework import serializers
from authentication.models import User, UserProfile
from dashboard.models import Dashboard


class UserDashboardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dashboard
        fields = '__all__'

