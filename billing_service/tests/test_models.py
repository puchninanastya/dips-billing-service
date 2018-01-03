from django.test import TestCase
from django.utils.timezone import now

from billing_service.models import Payment

class PaymentModelTestCase(TestCase):
    """This class defines the test suite for the Payment model."""

    def setUp(self):
        self.newCashPayment = Payment.objects.create(order_id=2,
            amount_paid=10000, payment_method='CH')
        self.newCardPayment = Payment.objects.create(order_id=3,
            amount_paid=14000, payment_method='CD',
            account_number='8736236426351234')

    def test_model_get_cash_payment(self):
        """Test the payment model can get cash payment."""
        payment = Payment.objects.get(pk=self.newCashPayment.id)
        self.assertEqual(payment.order_id, 2)
        self.assertEqual(payment.amount_paid, 10000)
        self.assertEqual(payment.payment_method, 'CH')

    def test_model_get_card_payment(self):
        """Test the payment model can get card payment."""
        payment = Payment.objects.get(pk=self.newCardPayment.id)
        self.assertEqual(payment.order_id, 3)
        self.assertEqual(payment.amount_paid, 14000)
        self.assertEqual(payment.payment_method, 'CD')
        self.assertEqual(payment.account_number, '8736236426351234')
