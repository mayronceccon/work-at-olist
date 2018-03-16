from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import PriceSerializer
from .models import Price
from .jsonschema import validate_price_data


@api_view(['GET'])
def get(request, pk=None):
    """
    Find a price per your id
    """
    calls = Price.objects.filter(pk=int(pk))
    serializer = PriceSerializer(calls, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all(request):
    """
    Find all prices
    """
    calls = Price.objects.all()
    serializer = PriceSerializer(calls, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def post(request):
    data = request.data
    valid = validate_price_data(data)
    if valid is not None:
        return Response(valid, status=status.HTTP_400_BAD_REQUEST)

    active = True
    if data['active'] == 'false':
        active = False
    data['active'] = active

    price = Price(
        price_fixed=data['price_fixed'],
        price_fractioned=data['price_fractioned'],
        start=data['start'],
        end=data['end'],
        active=data['active'],
    )
    result = price.save()

    return Response(result, status=status.HTTP_201_CREATED)
