from django.db import models
from cms.models import CMSPlugin
from filer.fields.image import FilerImageField

class NLSubscription(models.Model):
    subscriber_full_name = models.CharField(max_length=200, unique=True)
    subscriber_email = models.CharField(max_length=200, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('subscriber_full_name', 'subscriber_email')

