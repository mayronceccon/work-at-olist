from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PriceSerializer
from .models import Price


class PriceView(APIView):
    """
    get:
    Return a list of all the existing prices.
    """
    def get(self, request):
        calls = Price.objects.all()
        serializer = PriceSerializer(calls, many=True)
        return Response(serializer.data)
