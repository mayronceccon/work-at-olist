from rest_framework import serializers
from .models import Price


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = (
            'id', 'price_fixed', 'price_fractioned', 'start', 'end',
            'active'
            )
