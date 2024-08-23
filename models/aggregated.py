from django.db import models
from django.utils.translation import gettext_lazy as _


# CRM: Fotografie Mensili
class CRMMontlySnapshot(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    month = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    total_suppliers = models.IntegerField(null=True, blank=True)
    total_customers = models.IntegerField(null=True, blank=True)
    total_leads = models.IntegerField(null=True, blank=True)
    total_active_customers = models.IntegerField(null=True, blank=True)
    total_inactive_customers = models.IntegerField(null=True, blank=True)
    total_loyal_customers = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "CRM Monthly Snapshot"
        verbose_name_plural = "CRM Monthly Snapshots"

