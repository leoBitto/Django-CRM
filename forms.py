from django import forms
from .models.base import CompanyCategory, Company, Person

class CompanyCategoryForm(forms.ModelForm):
    class Meta:
        model = CompanyCategory
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome categoria'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrizione', 'rows': 3}),
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'category', 'website', 'phone', 'email', 'notes', 'is_own_company']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome azienda'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Indirizzo'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Sito web'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Note', 'rows': 3}),
            'is_own_company': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'phone', 'role', 'company']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cognome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono'}),
            'role': forms.Select(attrs={'class': 'form-select'}),
            'company': forms.Select(attrs={'class': 'form-select'}),
        }
