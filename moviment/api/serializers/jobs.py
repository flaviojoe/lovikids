from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from ...models import Job

class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'name', 'level']