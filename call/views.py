from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CallSerializer
from .models import Call


class CallView(APIView):
    """
    get:
    Return a list of all the existing calls.
    """
    def get(self, request):
        calls = Call.objects.all()
        serializer = CallSerializer(calls, many=True)
        return Response(serializer.data)
