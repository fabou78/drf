from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    '''
    DRF API View
    '''
    # request -> HttpRequest from Django
    # print(dir(request))
    # request.body

    data = {}
    model_data = Product.objects.all().order_by('?').first()
    if model_data:
        # serialisation using model_to_dict
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    # if model_data:
    #     # the below is serialisation the hard way
    #     data['id'] = model_data.id
    #     data['title'] = model_data.title
    #     data['content'] = model_data.content
    #     data['price'] = model_data.price

    return Response(data)
