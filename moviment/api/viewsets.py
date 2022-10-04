from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from moviment.models import JobExec, Job, Desire
from .serializers.jobs import JobSerializer
from .serializers.desires import DesireSerializer
from .serializers.jobexecs import JobExecSerializer


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class DesireViewSet(ModelViewSet):
    queryset = Desire.objects.all()
    serializer_class = DesireSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class JobExecViewSet(ModelViewSet):
    queryset = JobExec.objects.all()
    serializer_class = JobExecSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['user_id__first_name', 'job_id__name', 'desire_id__name']
