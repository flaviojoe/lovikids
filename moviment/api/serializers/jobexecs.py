from rest_framework import serializers
from moviment.models import JobExec


class JobExecSerializer(serializers.ModelSerializer):
    job_name = serializers.ReadOnlyField()
    desire_name = serializers.ReadOnlyField()
    user_name = serializers.ReadOnlyField()

    class Meta:
        model = JobExec
        fields = [
            'id', 'user_id', 'user_name',
            'job_id', 'job_name', 
            'desire_id', 'desire_name',
            'description', 'percent_done']