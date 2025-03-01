from django.urls import path
from . import views

app_name = 'crm'

urlpatterns = [
    # Company URLs
    path('companies/', views.CompanyListView.as_view(), name='company_list'),
    path('companies/<int:company_id>/', views.CompanyDetailView.as_view(), name='company_detail'),
    
    # Person URLs
    path('people/', views.PersonListView.as_view(), name='person_list'),
    path('people/<int:person_id>/', views.PersonDetailView.as_view(), name='person_detail'),
    
    # Company Category URLs
    path('categories/', views.CompanyCategoryListView.as_view(), name='category_list'),
    path('categories/<int:category_id>/', views.CompanyCategoryDetailView.as_view(), name='category_detail'),
]