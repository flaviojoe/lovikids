from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import DesireUserSerializer
from desire.models import DesireUser


class DesireUserViewSet(ModelViewSet):
    queryset = DesireUser.objects.all()
    serializer_class = DesireUserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)