# crm/models/aggregated.py
from django.db import models
from gold_bi.models import MonthlyAggregationBase

class CRMMontlyAggregation(MonthlyAggregationBase):
    total_suppliers = models.IntegerField(null=True, blank=True)
    total_customers = models.IntegerField(null=True, blank=True)
    total_leads = models.IntegerField(null=True, blank=True)
    total_active_customers = models.IntegerField(null=True, blank=True)
    total_inactive_customers = models.IntegerField(null=True, blank=True)
    total_loyal_customers = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "CRM Monthly Snapshot"
        verbose_name_plural = "CRM Monthly Snapshots"
