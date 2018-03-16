from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import PriceSerializer
from .models import Price


@api_view(['GET'])
def get(request, pk=None):
    """
    Comment get aaaa
    """
    calls = Price.objects.filter(pk=int(pk))
    serializer = PriceSerializer(calls, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all(request):
    """
    Comment get all
    """
    calls = Price.objects.all()
    serializer = PriceSerializer(calls, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
