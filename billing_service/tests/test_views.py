from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APIRequestFactory

from billing_service.models import Payment
from billing_service.serializers import PaymentSerializer
from billing_service.views import PaymentViewSet

class GetAllPaymentsTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()

        self.newCashPayment = Payment.objects.create(order_id=2,
            amount_paid=10000, payment_method='CH')
        self.newCardPayment = Payment.objects.create(order_id=3,
            amount_paid=14000, payment_method='CD',
            account_number='8736236426351234')

    def test_get_all_payments(self):
        """Test the api get payments."""
        # Setup.
        url = "/payments/"
        request = self.factory.get(url)
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        # Run.
        payment_list = PaymentViewSet.as_view({'get': 'list'})
        response = payment_list(request)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)

class GetSinglePaymentTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()

        self.newPayment = Payment.objects.create(order_id=3,
            amount_paid=14000, payment_method='CD',
            account_number='8736236426351234')

        self.invalid_pk = 2

    def test_get_valid_single_payment(self):
        """Test the api get valid single payment."""
        # Setup.
        url = "/payments/" + str(self.newPayment.pk)
        request = self.factory.get(url)
        serializer = PaymentSerializer(self.newPayment)
        # Run.
        payment_detail = PaymentViewSet.as_view({'get': 'retrieve'})
        response = payment_detail(request, pk=self.newPayment.pk)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_single_user(self):
        """Test the api get invalid single payment."""
        # Setup.
        url = "/payments/" + str(self.invalid_pk)
        request = self.factory.get(url)
        # Run.
        payment_detail = PaymentViewSet.as_view({'get': 'retrieve'})
        response = payment_detail(request, pk=self.invalid_pk)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewPaymentTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()

        self.valid_payload = {
            "order_id": 2,
            "payment_date": "2017-12-15T00:04:44.402571Z",
            "amount_paid": 7000,
            "payment_method": "CH",
            "account_number": ""
        }

        self.invalid_payload = {
            "payment_date": "2017-12-15T00:04:44.402571Z",
            "amount_paid": 7000,
            "payment_method": "CH",
            "account_number": ""
        }

    def test_create_valid_single_payment(self):
        """Test the api valid insert new payment."""
        # Setup.
        url = "/payments/"
        request = self.factory.post(url, self.valid_payload, format='json')
        # Run.
        payment_list = PaymentViewSet.as_view({'post': 'create'})
        response = payment_list(request)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_single_payment(self):
        """Test the api invalid insert new payment."""
        # Setup.
        url = "/payments/"
        request = self.factory.post(url, self.invalid_payload, format='json')
        # Run.
        payment_list = PaymentViewSet.as_view({'post': 'create'})
        response = payment_list(request)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSinglePaymentTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()

        self.newPayment = Payment.objects.create(order_id=3,
            amount_paid=14000, payment_method='CD',
            account_number='8736236426351234')

        self.invalid_pk = 2

    def test_delete_valid_single_payment(self):
        """Test the api valid delete new payment."""
        # Setup.
        url = "/payments/" + str(self.newPayment.pk)
        request = self.factory.delete(url)
        # Run.
        payment_detail = PaymentViewSet.as_view({'delete': 'destroy'})
        response = payment_detail(request, pk=self.newPayment.pk)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_valid_single_payment(self):
        """Test the api valid delete new payment."""
        # Setup.
        url = "/payments/" + str(self.invalid_pk)
        request = self.factory.delete(url)
        # Run.
        payment_detail = PaymentViewSet.as_view({'delete': 'destroy'})
        response = payment_detail(request, pk=self.invalid_pk)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
