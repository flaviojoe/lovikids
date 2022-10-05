from rest_framework import serializers
from desire.models import DesireUser


class DesireUserSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField()
    desire_name = serializers.ReadOnlyField()

    class Meta:
        model = DesireUser
        fields = ['id', 'user_id', 'user_name', 
            'desire_id', 'desire_name', 'description', 'status']