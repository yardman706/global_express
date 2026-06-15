from django.contrib import admin

from .models import QuoteRequest, Shipment, TrackingEvent


class TrackingEventInline(admin.TabularInline):
    model = TrackingEvent
    extra = 1
    fields = ('status', 'location', 'description', 'occurred_at')


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = (
        'tracking_number',
        'goods_description',
        'status',
        'origin',
        'destination',
        'estimated_delivery',
        'updated_at',
    )
    list_filter = ('status',)
    search_fields = ('tracking_number', 'goods_description', 'recipient_name', 'sender_name')
    inlines = [TrackingEventInline]


@admin.register(TrackingEvent)
class TrackingEventAdmin(admin.ModelAdmin):
    list_display = ('shipment', 'status', 'location', 'occurred_at')
    list_filter = ('status',)
    search_fields = ('shipment__tracking_number', 'location', 'description')


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'departure_city', 'delivery_city', 'weight', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'departure_city', 'delivery_city', 'phone')
    readonly_fields = ('created_at',)
