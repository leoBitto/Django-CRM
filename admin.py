from django.contrib import admin
from .models.base import CompanyCategory, Company, Person

class CompanyCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class PersonInline(admin.TabularInline):
    model = Person
    extra = 1
    autocomplete_fields = ['company']

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'vat_number', 'category', 'phone', 'email', 'is_own_company')
    list_filter = ('category', 'is_own_company')
    search_fields = ('name', 'address', 'email')
    inlines = [PersonInline]
    autocomplete_fields = ['category']

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role', 'company', 'email', 'phone')
    list_filter = ('role', 'company')
    search_fields = ('first_name', 'last_name', 'email', 'company__name')
    autocomplete_fields = ['company']

admin.site.register(CompanyCategory, CompanyCategoryAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Person, PersonAdmin)
