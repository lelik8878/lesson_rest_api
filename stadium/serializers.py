from enum import unique

from rest_framework import serializers

from stadium.models import PeopleCategory, CategoryOfService


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
        category_users = validated_data.pop('category_user')
        print(validated_data, '-2-2-2-2-2-2-2-2-2-2-2-2-2---------')
        people_category_instance = PeopleCategory.objects.create(**validated_data)
        for pre_create_dict in category_users:
            category_of_service_instance, created = CategoryOfService.objects.get_or_create(**pre_create_dict)
            people_category_instance.category_user.add(category_of_service_instance)
        return people_category_instance

