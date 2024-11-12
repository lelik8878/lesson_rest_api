from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    image = serializers.ImageField()
