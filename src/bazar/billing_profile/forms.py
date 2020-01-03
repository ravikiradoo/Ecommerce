from django import forms
from .models import Card

class PaymentForm(forms.Form):
    class Meta:
        model = Card
        fields = ('id')
