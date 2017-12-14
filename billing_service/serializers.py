from rest_framework import serializers

from .models import Payment

class Paymenterializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)
    class Meta:
        model = Payment
        fields = '__all__'
