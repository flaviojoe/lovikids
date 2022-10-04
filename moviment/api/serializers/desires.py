from rest_framework import serializers
from ...models import Desire

class DesireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desire
        fields = ['id', 'name', 'weight']