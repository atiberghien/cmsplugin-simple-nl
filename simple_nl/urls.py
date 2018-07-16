

from django.conf.urls import url
from .views import SubscriptionView

urlpatterns = [

    url(r'^subscribe/', SubscriptionView.as_view(),name="nl-subscribe"),
]