from rest_framework import serializers

from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)
    payment_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Payment
        fields = '__all__'
