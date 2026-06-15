from django.db import models
from django.utils import timezone


class Shipment(models.Model):
    class Status(models.TextChoices):
        ORDER_RECEIVED = 'order_received', 'Order Received'
        PICKED_UP = 'picked_up', 'Picked Up'
        IN_TRANSIT = 'in_transit', 'In Transit'
        OUT_FOR_DELIVERY = 'out_for_delivery', 'Out for Delivery'
        DELIVERED = 'delivered', 'Delivered'
        ON_HOLD = 'on_hold', 'On Hold'

    tracking_number = models.CharField(max_length=50, unique=True, db_index=True)
    goods_description = models.CharField(max_length=255)
    goods_weight = models.DecimalField(max_digits=8, decimal_places=2, help_text='Weight in kg')
    goods_height = models.DecimalField(max_digits=8, decimal_places=2, help_text='Height in cm')
    goods_width = models.DecimalField(max_digits=8, decimal_places=2, help_text='Width in cm')
    goods_length = models.DecimalField(max_digits=8, decimal_places=2, help_text='Length in cm')
    goods_value = models.DecimalField(max_digits=8, decimal_places=2, help_text='Value in Pounds')
    goods_type = models.CharField(max_length=50, help_text='Type of goods')
    quantity = models.PositiveIntegerField(default=1)
    sender_name = models.CharField(max_length=120)
    recipient_name = models.CharField(max_length=120)
    origin = models.CharField(max_length=120)
    destination = models.CharField(max_length=120)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ORDER_RECEIVED,
    )
    estimated_delivery = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f'{self.tracking_number} — {self.goods_description}'

    @property
    def is_delivered(self):
        return self.status == self.Status.DELIVERED


class TrackingEvent(models.Model):
    shipment = models.ForeignKey(
        Shipment,
        related_name='events',
        on_delete=models.CASCADE,
    )
    status = models.CharField(max_length=20, choices=Shipment.Status.choices)
    location = models.CharField(max_length=120)
    description = models.TextField()
    occurred_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-occurred_at']

    def __str__(self):
        return f'{self.shipment.tracking_number} — {self.get_status_display()}'


class QuoteRequest(models.Model):
    departure_city = models.CharField(max_length=120)
    delivery_city = models.CharField(max_length=120)
    weight = models.CharField(max_length=50)
    dimensions = models.CharField(max_length=50)
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.departure_city} to {self.delivery_city}'


class ContactRequest(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.email}'