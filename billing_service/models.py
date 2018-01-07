from django.db import models
from django.core.validators import RegexValidator
from django.utils.timezone import now

class Payment(models.Model):
    order_id = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="For order")
    payment_date = models.DateTimeField(
        blank=True,
        null=False,
        default=now,
        verbose_name="Payment datetime")
    amount_paid = models.PositiveIntegerField(
        verbose_name="Amount paid")
    payment_method = models.CharField(
        max_length=2,
        blank=True,
        null=False,
        default='CH',
        choices=(
            ('CH', 'Cash payment'),
            ('CD', 'Payment by card')),
        verbose_name="Payment method")
    account_number_regex = RegexValidator(
        regex=r'^\d{,20}$',
        message="This field should contain only digits."
    )
    account_number = models.CharField(
        validators=[account_number_regex],
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Account number")

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self):
        return "id {}".format(self.pk)
