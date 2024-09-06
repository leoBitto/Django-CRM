import logging
from django.utils import timezone
from crm.models.aggregated import CRMMontlyAggregation
from django.db import transaction
from crm.models.base import *
from backoffice.utils import *

logger = logging.getLogger('tasks')

def aggregate_crm_monthly():
    try:
        today = get_today()
        date_params, _ = get_month_params(today)

        # Aggregazione dei dati
        total_suppliers = Supplier.objects.using('default').count()
        total_customers = Customer.objects.using('default').count()
        total_leads = Customer.objects.using('default').filter(status='LEAD').count()
        total_active_customers = Customer.objects.using('default').filter(status='ACTIVE').count()
        total_inactive_customers = Customer.objects.using('default').filter(status='INACTIVE').count()
        total_loyal_customers = Customer.objects.using('default').filter(status='LOYAL').count()

        crm_aggregations = {
            'total_suppliers': total_suppliers,
            'total_customers': total_customers,
            'total_leads': total_leads,
            'total_active_customers': total_active_customers,
            'total_inactive_customers': total_inactive_customers,
            'total_loyal_customers': total_loyal_customers
        }

        with transaction.atomic():
            CRMMontlyAggregation.objects.using('gold').update_or_create(
                month=date_params['month'],
                year=date_params['year'],
                defaults=crm_aggregations
            )

        logger.info(f'Monthly CRM logs aggregated successfully for {date_params["month"]} / {date_params["year"]}.')
    except Exception as e:
        logger.error(f'Error aggregating monthly CRM logs: {e}')
