from rest_framework.views import APIView
from rest_framework.response import Response


class PricesView(APIView):
    """
    get:
    Return a list of all the existing prices.
    """
    def get(self, request):
        return Response({'test': 'It worked!'})
