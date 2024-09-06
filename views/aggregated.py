# crm/views/aggregated.py
from django.shortcuts import render
from crm.models.aggregated import *
import logging
logger = logging.getLogger('reports')
from django.views import View
from backoffice.forms import MonthlyAggregationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from backoffice.utils import *

class CRMReportView(LoginRequiredMixin, View):
    template_name = 'backoffice/reports/select_aggregation.html'

    def get(self, request, *args, **kwargs):
        context = {
            'monthly_form': MonthlyAggregationForm(),
            'report_type': 'CRM',
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = None
        aggregation_model = None
        period_type = None
        selected_period = None

        if 'monthly_submit' in request.POST:
                form = MonthlyAggregationForm(request.POST)
                if form.is_valid():
                    aggregation_model = CRMMontlyAggregation
                    period_type = 'month'
                    selected_period = {
                        'month': form.cleaned_data['month'],
                        'year': form.cleaned_data['year']
                    }

        if form and form.is_valid():
            # Ottieni i dati per i 6 periodi precedenti
            previous_periods_data = get_previous_periods(
                aggregation_model, selected_period, period_type, num_previous_periods=6
            )

            return render(request, 'crm/reports/crm_report.html', {
                'data': previous_periods_data,
                'report_type': 'CRM',
                'period_type': period_type,
            })

        context = {
            'monthly_form': form if 'monthly_submit' in request.POST else MonthlyAggregationForm(),
            'report_type': 'CRM',
        }
        return render(request, self.template_name, context)


