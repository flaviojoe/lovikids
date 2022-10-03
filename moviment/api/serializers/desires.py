from rest_framework import serializers
from ...models import Desire

class DesireSerializers(serializers.ModelSerializer):
    class Meta:
        model = Desire
        fields = ['id', 'name', 'weight']