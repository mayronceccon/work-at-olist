from rest_framework.views import APIView
from rest_framework.response import Response


class PricesView(APIView):
    def get(self, request):
        return Response({'test': 'It worked!'})
