from django.contrib import admin
from .models import Company, Supplier, Customer

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('company',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'email', 'phone', 'status')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('company', 'status')
