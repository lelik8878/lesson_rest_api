from enum import unique

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


class PeopleCategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255,required=True)
    last_name = serializers.CharField(max_length=255, required=True)
    category_user = CategoryOfServiceSerializer(many=True)

    def create(self, validated_data):
        print(validated_data, '--------------------')
        for pre_create_dict in validated_data:
            pass
            # print(pre_create_dict)
            # name = validated_data.pop('name')
