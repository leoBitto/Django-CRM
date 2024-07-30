from django.urls import path
from .views import CompanyView, SupplierView, CustomerView

app_name = 'crm'

urlpatterns = [
    path('companies/', CompanyView.as_view(), name='company_view'),
    path('suppliers/', SupplierView.as_view(), name='supplier_view'),
    path('customers/', CustomerView.as_view(), name='customer_view'),
]
