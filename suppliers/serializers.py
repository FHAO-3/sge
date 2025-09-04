from rest_framework import serializers
from . import models


class SupplierSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Supplier
        fields = '__all__'
