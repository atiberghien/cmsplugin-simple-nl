from django.contrib import admin
from django.http import HttpResponse

from .models import NLSubscription

import csv


class NLSubscriptionAdmin(admin.ModelAdmin):
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        # writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export CSV"

    list_display = ('subscriber_full_name', 'subscriber_email', 'date')
    actions = ["export_as_csv"]


admin.site.register(NLSubscription, NLSubscriptionAdmin)
