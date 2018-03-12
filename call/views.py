from rest_framework.views import APIView
from rest_framework.response import Response


class CallView(APIView):
    """
    get:
    Return a list of all the existing calls.
    """
    def get(self, request):
        return Response({'test': 'It worked!'})
