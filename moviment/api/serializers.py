from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from moviment.models import JobExec
from core.models import Job


class JobExecSerializer(ModelSerializer):
    # job = PrimaryKeyRelatedField(queryset=Job.objects.select_related('name').all())

    class Meta:
        model = JobExec
        fields = ['id', 'description']
