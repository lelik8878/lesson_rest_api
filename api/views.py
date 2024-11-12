from django.db.models.signals import pre_save
from django.http import HttpResponse, FileResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Product
from api.serializers import ProductSerializer
from api.forms import SaveDataForm


from stadium.models import CategoryOfService, TypeOfService


@api_view(['GET', 'POST'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    if request.method == 'POST':
        print(request.data)
        # return Response()
    # print(serializer)
    # if serializer.is_valid():
    print(serializer.data)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def save_data_to_db(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        # print(request.body)
        # restored_object = json.loads(request.body)
        # print(restored_object)
        # print(restored_object['name'])
        # print(restored_object['price'])
        # print(restored_object['image'])
        # pre_save_object = Product(name=restored_object['name'],
        #                           price=restored_object['price'])
        # print(pre_save_object)
        # pre_save_object.save()
        serializer = ProductSerializer(data=request.data)
        # print(serializer)
        if serializer.is_valid():
            print(serializer.validated_data)
            print(serializer.data)
            pre_save_data = Product(name=serializer.validated_data['name'],
                                    price=serializer.validated_data['price'],
                                    image=serializer.validated_data['image'])
            pre_save_data.save()

        print(serializer.errors)
    answer = open(r'C:\Users\100nout\PycharmProjects\lesson_rest_api\media\Cheque_001.pdf', 'rb')
    return FileResponse({'first_message': 'Well done'}, filename=r'C:\Users\100nout\PycharmProjects\lesson_rest_api\media\Cheque_001.pdf')
