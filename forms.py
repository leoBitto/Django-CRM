# crm/forms.py

from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Company, Supplier, Customer

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address']
        labels = {
            'name': _('Nome'),
            'address': _('Indirizzo'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': _('Inserisci il nome della azienda')})
        self.fields['address'].widget.attrs.update({'placeholder': _('Inserisci l\'indirizzo della azienda')})

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'company', 'email', 'phone']
        labels = {
            'name': _('Nome'),
            'company': _('Azienda'),
            'email': _('Email'),
            'phone': _('Telefono'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': _('Inserisci il nome del fornitore')})
        self.fields['email'].widget.attrs.update({'placeholder': _('Inserisci l\'email del fornitore')})
        self.fields['phone'].widget.attrs.update({'placeholder': _('Inserisci il telefono del fornitore')})

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'company', 'email', 'phone', 'status']
        labels = {
            'name': _('Nome'),
            'company': _('Azienda'),
            'email': _('Email'),
            'phone': _('Telefono'),
            'status': _('Stato'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': _('Inserisci il nome del cliente')})
        self.fields['email'].widget.attrs.update({'placeholder': _('Inserisci l\'email del cliente')})
        self.fields['phone'].widget.attrs.update({'placeholder': _('Inserisci il telefono del cliente')})
