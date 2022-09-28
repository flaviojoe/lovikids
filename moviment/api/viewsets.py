from rest_framework.viewsets import ModelViewSet
from moviment.models import JobExec
from .serializers import JobExecSerializer

class JobExecViewSet(ModelViewSet):
    queryset = JobExec.objects.all()
    serializer_class = JobExecSerializer