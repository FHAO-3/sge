from rest_framework import serializers
from . import models


class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = '__all__'
