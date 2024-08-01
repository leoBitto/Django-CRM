from django.contrib import admin
from .models import CompanyCategory, Company, Supplier, Customer

@admin.register(CompanyCategory)
class CompanyCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'category', 'phone', 'email', 'website')
    list_filter = ('type', 'category')
    search_fields = ('name', 'address', 'phone', 'email')
    ordering = ('name',)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'phone', 'email')
    list_filter = ('company',)
    search_fields = ('name', 'phone', 'email', 'company__name')
    ordering = ('name',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'status', 'phone', 'email')
    list_filter = ('status', 'company')
    search_fields = ('name', 'phone', 'email', 'company__name')
    ordering = ('name',)
