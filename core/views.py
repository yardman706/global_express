from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import QuoteRequestForm
from .models import Shipment


def _get_shipment(tracking_number):
    if not tracking_number:
        return None
    return (
        Shipment.objects.filter(tracking_number__iexact=tracking_number)
        .prefetch_related('events')
        .first()
    )


def home(request):
    return render(request, 'core/index.html')


def track(request):
    tracking_number = request.GET.get('tracking', '').strip()
    shipment = _get_shipment(tracking_number)

    return render(request, 'core/track.html', {
        'tracking_number': tracking_number,
        'shipment': shipment,
    })


def get_quote(request):
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your quote request has been sent successfully. Our team will contact you shortly.',
            )
            return redirect('get_quote')
    else:
        form = QuoteRequestForm()

    return render(request, 'core/get_quote.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully. Our team will contact you shortly.')
            return redirect('contact')
    else:
        form = ContactRequestForm()
    return render(request, 'core/contact.html', {'form': form})