# crm/forms.py

from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Company, Supplier, Customer, CompanyCategory


class CompanyCategoryForm(forms.ModelForm):
    class Meta:
        model = CompanyCategory
        fields = ['name', 'description']
        labels = {
            'name': _('Nome'),
            'description': _('Descrizione'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': _('Inserisci il nome della categoria')})
       


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'category', 'type', 'website', 'phone', 'email', 'notes']
        labels = {
            'name': _('Nome'),
            'address': _('Indirizzo'),
            'category': _('Categoria'),
            'type': _('Tipologia'),
            'website': _('Sito Web'),
            'phone': _('Telefono'),
            'email': _('Email'),
            'notes': _('Note'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': _('Inserisci il nome della azienda')})
        self.fields['address'].widget.attrs.update({'placeholder': _('Inserisci l\'indirizzo della azienda')})
        self.fields['phone'].widget.attrs.update({'placeholder': _('Inserisci il numero di telefono')})
        self.fields['email'].widget.attrs.update({'placeholder': _('Inserisci l\'email')})
        self.fields['website'].widget.attrs.update({'placeholder': _('Inserisci il sito web (opzionale)')})
        self.fields['notes'].widget.attrs.update({'placeholder': _('Inserisci eventuali note (opzionale)')})


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'company', 'email', 'phone', 'notes']
        labels = {
            'name': _('Nome'),
            'company': _('Azienda'),
            'email': _('Email'),
            'phone': _('Telefono'),
            'notes': _('Note'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': _('Inserisci il nome del fornitore')})
        self.fields['company'].queryset = Company.objects.filter(type='Supplier')
        self.fields['email'].widget.attrs.update({'placeholder': _('Inserisci l\'email del fornitore')})
        self.fields['phone'].widget.attrs.update({'placeholder': _('Inserisci il telefono del fornitore')})
        self.fields['notes'].widget.attrs.update({'placeholder': _('Inserisci eventuali note (opzionale)')})


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
        self.fields['company'].queryset = Company.objects.filter(type='Customer')
        self.fields['email'].widget.attrs.update({'placeholder': _('Inserisci l\'email del cliente')})
        self.fields['phone'].widget.attrs.update({'placeholder': _('Inserisci il telefono del cliente')})
        self.fields['status'].widget.attrs.update({'placeholder': _('Seleziona lo stato del cliente')})
