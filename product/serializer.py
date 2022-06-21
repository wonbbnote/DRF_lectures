from rest_framework import serializers

from .models import Product as ProductModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ["id","title", "description", "writer", "exposure_start_date","exposure_end_date", "thumbnail" ]

    