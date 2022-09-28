from dataclasses import fields
import imp
from pyclbr import Class
from pyexpat import model
from urllib.request import CacheFTPHandler
from rest_framework.serializers import ModelSerializer, StringRelatedField
from moviment.models import JobExec


class JobExecSerializer(ModelSerializer):
    name = StringRelatedField()

    class Meta:
        model = JobExec
        fields = ['id', 'name']
