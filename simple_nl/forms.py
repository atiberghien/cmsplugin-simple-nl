from django import forms
from .models import NLSubscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = NLSubscription
        fields = ("subscriber_full_name", "subscriber_email")