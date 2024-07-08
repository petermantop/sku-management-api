from rest_framework import serializers
from skus.models import Sku


class SkuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sku
        fields = ['id', 'medication_name', 'dose', 'presentation', 'unit', 'countries']