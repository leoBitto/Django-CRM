from django.urls import path
from crm.views.base import *

app_name = 'crm'

urlpatterns = [
    # Company URLs
    path('companies/', CompanyListView.as_view(), name='company_list'),
    path('companies/<int:company_id>/', CompanyDetailView.as_view(), name='company_detail'),
    
    # Person URLs
    path('people/', PersonListView.as_view(), name='person_list'),
    path('people/<int:person_id>/', PersonDetailView.as_view(), name='person_detail'),
    
    # Company Category URLs
    path('categories/', CompanyCategoryListView.as_view(), name='category_list'),
    path('categories/<int:category_id>/', CompanyCategoryDetailView.as_view(), name='category_detail'),
]