from django import forms

from .models import QuoteRequest, ContactRequest


class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = (
            'departure_city',
            'delivery_city',
            'weight',
            'dimensions',
            'name',
            'email',
            'phone',
            'message',
        )
        widgets = {
            'departure_city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City of Departure',
            }),
            'delivery_city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Delivery City',
            }),
            'weight': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Total Weight (kg)',
            }),
            'dimensions': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dimensions (cm)',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us about your shipment',
                'rows': 6,
            }),
        }


class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ('name', 'email', 'phone', 'message')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
            }),
        }