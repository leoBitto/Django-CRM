from django.urls import path
from .views.base import CompanyView, SupplierView, CustomerView, CompanyCategoryView
from crm.views.aggregated import CRMReportView

app_name = 'crm'

urlpatterns = [
    path('company_categories/', CompanyCategoryView.as_view(), name='company_categories_view'),
    path('companies/', CompanyView.as_view(), name='company_view'),
    path('suppliers/', SupplierView.as_view(), name='supplier_view'),
    path('customers/', CustomerView.as_view(), name='customer_view'),

    path('crm_report', CRMReportView.as_view(), name='crm_report'),
]
