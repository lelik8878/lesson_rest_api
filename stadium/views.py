from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import json

from stadium.models import CategoryOfService, TypeOfService, TypeOfSubService
from stadium.serializers import (CategoryOfServiceSerializer, TypeOfServiceSerializer,
                                 TypeOfServiceSerializerExcludeForeignKey, TypeOfSubServiceSerializer,
                                 SpecificObjectSerializer, PeopleCategorySerializer)


@api_view(['GET'])
def get_category_of_service(request):
    categories = CategoryOfService.objects.all()
    serializer = CategoryOfServiceSerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_type_of_services(request):
    type_of_services = TypeOfService.objects.all()
    serializer = TypeOfServiceSerializer(type_of_services, many=True)
    initial_serializer = TypeOfServiceSerializerExcludeForeignKey(type_of_services, many=True)
    return Response(initial_serializer.data)

@api_view(['GET'])
def get_type_of_sub_services(request):
    type_of_sub_services = TypeOfSubService.objects.all()
    serializer = TypeOfSubServiceSerializer(type_of_sub_services, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_specific_object(request):
    categories = CategoryOfService.objects.all()
    serializer = SpecificObjectSerializer(categories, many=True)
    return Response(serializer.data)

class Category(APIView):
    def post(self, request):
        serializer = CategoryOfServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'message': 'Johan'})

    def get(self, request):
        return Response({'message': 'Johan'})

    def put(self, request):
        return Response({'message': 'Johan'})

    def delete(self, request):
        return Response({'message': 'Johan'})


@api_view(['GET', 'POST'])
def save_or_create(request):
    json_data = '''{
    "title": "Частным лицам2",
    "service_set": [
    {
      "title": "petux",
      "image": "/media/service/logo.png",
      "description": "fdsagdfsgdsf",
      "best": true
    },
    {
      "title": "petux3",
      "image": "/media/service/logo.png",
      "description": "fdsagdfsgdsf",
      "best": true
      }
     ]
    }'''
    parsed_json = json.loads(json_data)
    category_of_service_instance = CategoryOfService.objects.filter(title=parsed_json['title']).first()
    new_category_of_service = CategoryOfService(title=parsed_json['title'])
    print(new_category_of_service)
    if category_of_service_instance:
        for i in parsed_json['service_set']:
            type_of_service_instance = TypeOfService.objects.filter(title=i['title']).first()
            if not type_of_service_instance:
                new_type_of_service = TypeOfService(title=i['title'],
                                                    image=i['image'],
                                                    description=i['description'],
                                                    best=i['best'],
                                                    category_of_service_id=category_of_service_instance)
                print(new_type_of_service.__dict__)
                #new_type_of_service.save()
    else:
        print('Not Exist')
        #new_category_of_service.save()
        for i in parsed_json['service_set']:
            type_of_service_instance = TypeOfService.objects.filter(title=i['title']).first()
            if not type_of_service_instance:
                new_type_of_service = TypeOfService(title=i['title'],
                                                    image=i['image'],
                                                    description=i['description'],
                                                    best=i['best'],
                                                    category_of_service_id=new_category_of_service)
                print(new_type_of_service.__dict__)
                #new_type_of_service.save()
    return Response({"message": "Johan"})


class PeopleListView(APIView):
    def get(self, request):
        return Response({"message": "Johan"})

    def post(self, request):
        received_data_from_victor = [{
        "name": "Иван",
        "last_name": "Иванов",
        "category_user": [
            {
                "title": "Консультации"
            },
            {
                "title": "Обучение"
            }
        ]
        },
        {
            "name": "Мария",
            "last_name": "Петрова",
            "category_user": [
                {
                    "title": "Консультации"
                }
            ]
        },
        {
            "name": "Алексей",
            "last_name": "Сидоров",
            "category_user": [
                {
                    "title": "Поддержка"
                },
                {
                    "title": "Обучение"
                }
            ]
        }]
        received_data = PeopleCategorySerializer(data=received_data_from_victor, many=True)
        if received_data.is_valid():
            print(received_data.validated_data, '+++++++++++++++++')
            # received_data.create(received_data.validated_data)
            return Response({"message": "success"})
        return Response(received_data.errors)

