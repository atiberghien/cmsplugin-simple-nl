from django.views.generic import CreateView
from .forms import SubscriptionForm
from .models import NLSubscription

class SubscriptionView(CreateView):
    model = NLSubscription
    form_class = SubscriptionForm
    success_url = "/"