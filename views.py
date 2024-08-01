from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy
from .models import Company, Supplier, Customer, CompanyCategory
from .forms import CompanyForm, SupplierForm, CustomerForm, CompanyCategoryForm
from django.contrib import messages


class CompanyCategoryView(LoginRequiredMixin, View):
    template_name = 'crm/company_category.html'

    def get(self, request, *args, **kwargs):
        categories = CompanyCategory.objects.all()
        category_form = CompanyCategoryForm()
        return render(request, self.template_name, {
            'categories': categories,
            'company_category_form': category_form,
        })

    def post(self, request, *args, **kwargs):
        if 'create_category' in request.POST:
            category_form = CompanyCategoryForm(request.POST)
            if category_form.is_valid():
                category_form.save()
                messages.success(request, 'Categoria aziendale creata con successo.')
                return redirect('crm:company_categories_view')
            else:
                messages.error(request, 'Errore nella creazione della categoria aziendale.')
        
        elif 'update_category' in request.POST:
            category_id = request.POST.get('category_id')
            category = get_object_or_404(CompanyCategory, id=category_id)
            category_form = CompanyCategoryForm(request.POST, instance=category)
            if category_form.is_valid():
                category_form.save()
                messages.success(request, 'Categoria aziendale aggiornata con successo.')
                return redirect('crm:company_categories_view')
            else:
                messages.error(request, 'Errore nell\'aggiornamento della categoria aziendale.')
        
        elif 'delete_category' in request.POST:
            category_id = request.POST.get('category_id')
            category = get_object_or_404(CompanyCategory, id=category_id)
            category.delete()
            messages.success(request, 'Categoria aziendale eliminata con successo.')
            return redirect('crm:company_categories_view')
        
        categories = CompanyCategory.objects.all()
        return render(request, self.template_name, {
            'categories': categories,
            'category_form': category_form,
        })

class CompanyView(LoginRequiredMixin, View):
    template_name = 'crm/company.html'
    
    def get(self, request, *args, **kwargs):
        companies = Company.objects.all()
        company_form = CompanyForm()
        return render(request, self.template_name, {
            'companies': companies,
            'company_form': company_form,
        })

    def post(self, request, *args, **kwargs):
        if 'create_company' in request.POST:
            company_form = CompanyForm(request.POST)
            if company_form.is_valid():
                company_form.save()
                messages.success(request, 'Azienda creata con successo.')
                return redirect('crm:company_view')
            else:
                messages.error(request, 'Errore nella creazione dell\'azienda.')
        
        elif 'update_company' in request.POST:
            company_id = request.POST.get('company_id')
            company = get_object_or_404(Company, id=company_id)
            company_form = CompanyForm(request.POST, instance=company)
            if company_form.is_valid():
                company_form.save()
                messages.success(request, 'Azienda aggiornata con successo.')
                return redirect('crm:company_view')
            else:
                messages.error(request, 'Errore nell\'aggiornamento dell\'azienda.')
        
        elif 'delete_company' in request.POST:
            company_id = request.POST.get('company_id')
            company = get_object_or_404(Company, id=company_id)
            company.delete()
            messages.success(request, 'Azienda eliminata con successo.')
            return redirect('crm:company_view')
        
        companies = Company.objects.all()
        return render(request, self.template_name, {
            'companies': companies,
            'company_form': company_form,
        })

class SupplierView(LoginRequiredMixin, View):
    template_name = 'crm/supplier.html'
    
    def get(self, request, *args, **kwargs):
        suppliers = Supplier.objects.all()
        supplier_form = SupplierForm()
        return render(request, self.template_name, {
            'suppliers': suppliers,
            'supplier_form': supplier_form,
        })

    def post(self, request, *args, **kwargs):
        if 'create_supplier' in request.POST:
            supplier_form = SupplierForm(request.POST)
            if supplier_form.is_valid():
                supplier_form.save()
                messages.success(request, 'Fornitore creato con successo.')
                return redirect('crm:supplier_view')
            else:
                messages.error(request, 'Errore nella creazione del fornitore.')
        
        elif 'update_supplier' in request.POST:
            supplier_id = request.POST.get('supplier_id')
            supplier = get_object_or_404(Supplier, id=supplier_id)
            supplier_form = SupplierForm(request.POST, instance=supplier)
            if supplier_form.is_valid():
                supplier_form.save()
                messages.success(request, 'Fornitore aggiornato con successo.')
                return redirect('crm:supplier_view')
            else:
                messages.error(request, 'Errore nell\'aggiornamento del fornitore.')
        
        elif 'delete_supplier' in request.POST:
            supplier_id = request.POST.get('supplier_id')
            supplier = get_object_or_404(Supplier, id=supplier_id)
            supplier.delete()
            messages.success(request, 'Fornitore eliminato con successo.')
            return redirect('crm:supplier_view')
        
        suppliers = Supplier.objects.all()
        return render(request, self.template_name, {
            'suppliers': suppliers,
            'supplier_form': supplier_form,
        })

class CustomerView(LoginRequiredMixin, View):
    template_name = 'crm/customer.html'
    
    def get(self, request, *args, **kwargs):
        customers = Customer.objects.all()
        customer_form = CustomerForm()
        return render(request, self.template_name, {
            'customers': customers,
            'customer_form': customer_form,
        })

    def post(self, request, *args, **kwargs):
        if 'create_customer' in request.POST:
            customer_form = CustomerForm(request.POST)
            if customer_form.is_valid():
                customer_form.save()
                messages.success(request, 'Cliente creato con successo.')
                return redirect('crm:customer_view')
            else:
                messages.error(request, 'Errore nella creazione del cliente.')
        
        elif 'update_customer' in request.POST:
            customer_id = request.POST.get('customer_id')
            customer = get_object_or_404(Customer, id=customer_id)
            customer_form = CustomerForm(request.POST, instance=customer)
            if customer_form.is_valid():
                customer_form.save()
                messages.success(request, 'Cliente aggiornato con successo.')
                return redirect('crm:customer_view')
            else:
                messages.error(request, 'Errore nell\'aggiornamento del cliente.')
        
        elif 'delete_customer' in request.POST:
            customer_id = request.POST.get('customer_id')
            customer = get_object_or_404(Customer, id=customer_id)
            customer.delete()
            messages.success(request, 'Cliente eliminato con successo.')
            return redirect('crm:customer_view')
        
        customers = Customer.objects.all()
        return render(request, self.template_name, {
            'customers': customers,
            'customer_form': customer_form,
        })
