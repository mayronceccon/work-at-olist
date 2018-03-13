from rest_framework import serializers
from .models import Call


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = (
            'id', 'type', 'start', 'end', 'call_id_external',
            'source', 'destination'
            )
