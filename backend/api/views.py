# from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    '''
    DRF API View
    '''
    # request -> HttpRequest from Django
    # print(dir(request))
    # request.body

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({'invalid': 'not good data'}, status=400)

    # data = {}
    # instance = Product.objects.all().order_by('?').first()
    # if instance:
    #     data = ProductSerializer(instance).data

    # model_data = Product.objects.all().order_by('?').first()
    # if model_data:
    #     # serialisation using model_to_dict
    #     data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    # if model_data:
    #     # the below is serialisation the hard way
    #     data['id'] = model_data.id
    #     data['title'] = model_data.title
    #     data['content'] = model_data.content
    #     data['price'] = model_data.price

    return Response(data)
