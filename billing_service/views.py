from django.shortcuts import render

from rest_framework import viewsets, mixins
from rest_framework import status

from .serializers import PaymentSerializer
from .models import Payment

#TODO: Create tests for views

class PaymentViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
