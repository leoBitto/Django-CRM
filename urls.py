from django.urls import path
from crm.views import CompanyListView, CompanyDetailView, PersonListView, PersonDetailView, CompanyCategoryListView, CompanyCategoryDetailView

app_name = 'crm'

urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='company_list'),
    path('companies/<int:company_id>/', CompanyDetailView.as_view(), name='company_detail'),
    path('person/', PersonListView.as_view(), name='person_list'),
    path('person/<int:person_id>/', PersonDetailView.as_view(), name='person_detail'),
    path('company_categories/', CompanyCategoryListView.as_view(), name='category_list'),
    path('company_categories/<int:category_id>/', CompanyCategoryDetailView.as_view(), name='category_detail'),
]
