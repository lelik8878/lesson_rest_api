from rest_framework import serializers


class CategoryOfServiceSerializer(serializers.Serializer):
    title = serializers.CharField()





class TypeOfServiceSerializer(serializers.Serializer):
    # typeofsubservice_set = TypeOfSubServiceSerializer(many=True)
    title = serializers.CharField()
    image = serializers.ImageField()
    description = serializers.CharField()
    best =serializers.BooleanField()


class TypeOfSubServiceSerializer(serializers.Serializer):
    title = serializers.CharField()
    unit = serializers.CharField()
    price = serializers.DecimalField(max_digits=7, decimal_places=2)


class TypeOfServiceSerializerExcludeForeignKey(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.ImageField()
    description = serializers.CharField()
    best =serializers.BooleanField()
    typeofsubservice_set = TypeOfSubServiceSerializer(many=True)



class SpecificObjectSerializer(serializers.Serializer):
    title = serializers.CharField()
    typeofservice_set = TypeOfServiceSerializerExcludeForeignKey(many=True)
