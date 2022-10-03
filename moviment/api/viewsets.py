from rest_framework.viewsets import ModelViewSet
from moviment.models import JobExec, Job, Desire
from .serializers.jobs import JobSerializers
from .serializers.desires import DesireSerializers

class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializers

class DesireViewSet(ModelViewSet):
    queryset = Desire.objects.all()
    serializer_class = DesireSerializers