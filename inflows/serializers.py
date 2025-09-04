from rest_framework import serializers
from . import models


class InflowSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Inflow
        fields = '__all__'
