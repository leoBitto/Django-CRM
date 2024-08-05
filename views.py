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
        category_info = []

        # Creare un modulo per ogni categoria
        for category in categories:
            form = CompanyCategoryForm(instance=category)
            category_info.append({'category': category, 'form': form})

        # Aggiungere un modulo vuoto per la creazione di nuove categorie
        create_form = CompanyCategoryForm()

        return render(request, self.template_name, {
            'category_info': category_info,
            'create_form': create_form,
        })

    def post(self, request, *args, **kwargs):
        if 'create_category' in request.POST:
            category_form = CompanyCategoryForm(request.POST)
            if category_form.is_valid():
                category_form.save()
                messages.success(request, 'Categoria aziendale creata con successo.')
                return redirect('crm:company_categories_view')
            else:
                for field, errors in category_form.errors.items():
                    for error in errors:
                        messages.error(request, f"Errore nel campo '{field}': {error}")
        
        elif 'update_category' in request.POST:
            category_id = request.POST.get('category_id')
            category = get_object_or_404(CompanyCategory, id=category_id)
            category_form = CompanyCategoryForm(request.POST, instance=category)
            if category_form.is_valid():
                category_form.save()
                messages.success(request, 'Categoria aziendale aggiornata con successo.')
                return redirect('crm:company_categories_view')
            else:
                for field, errors in category_form.errors.items():
                    for error in errors:
                        messages.error(request, f"Errore nel campo '{field}': {error}")
        
        elif 'delete_category' in request.POST:
            category_id = request.POST.get('category_id')
            category = get_object_or_404(CompanyCategory, id=category_id)
            category.delete()
            messages.success(request, 'Categoria aziendale eliminata con successo.')
            return redirect('crm:company_categories_view')
        
        # Se si arriva qui, non è stato fatto nulla di valido
        categories = CompanyCategory.objects.all()
        category_info = []

        for category in categories:
            form = CompanyCategoryForm(instance=category)
            category_info.append({'category': category, 'form': form})

        create_form = CompanyCategoryForm()

        return render(request, self.template_name, {
            'category_info': category_info,
            'create_form': create_form,
        })


class CompanyView(LoginRequiredMixin, View):
    template_name = 'crm/company.html'
    
    def get(self, request, *args, **kwargs):
        companies = Company.objects.all()
        company_info = []

        # Creare un modulo per ogni azienda
        for company in companies:
            form = CompanyForm(instance=company)
            company_info.append({'company': company, 'form': form})

        # Aggiungere un modulo vuoto per la creazione di nuove aziende
        create_form = CompanyForm()

        return render(request, self.template_name, {
            'company_info': company_info,
            'create_form': create_form,
        })

    def post(self, request, *args, **kwargs):
        if 'create_company' in request.POST:
            company_form = CompanyForm(request.POST)
            if company_form.is_valid():
                company_form.save()
                messages.success(request, 'Azienda creata con successo.')
                return redirect('crm:company_view')
            else:
                for field, errors in company_form.errors.items():
                    for error in errors:
                        messages.error(request, f"Errore nel campo '{field}': {error}")
        
        elif 'update_company' in request.POST:
            company_id = request.POST.get('company_id')
            company = get_object_or_404(Company, id=company_id)
            company_form = CompanyForm(request.POST, instance=company)
            if company_form.is_valid():
                company_form.save()
                messages.success(request, 'Azienda aggiornata con successo.')
                return redirect('crm:company_view')
            else:
                for field, errors in company_form.errors.items():
                    for error in errors:
                        messages.error(request, f"Errore nel campo '{field}': {error}")
        
        elif 'delete_company' in request.POST:
            company_id = request.POST.get('company_id')
            company = get_object_or_404(Company, id=company_id)
            company.delete()
            messages.success(request, 'Azienda eliminata con successo.')
            return redirect('crm:company_view')
        
        # Se si arriva qui, non è stato fatto nulla di valido
        companies = Company.objects.all()
        company_info = []

        for company in companies:
            form = CompanyForm(instance=company)
            company_info.append({'company': company, 'form': form})

        create_form = CompanyForm()

        return render(request, self.template_name, {
            'company_info': company_info,
            'create_form': create_form,
        })


class SupplierView(LoginRequiredMixin, View):
    template_name = 'crm/supplier.html'
    
    def get(self, request, *args, **kwargs):
        suppliers = Supplier.objects.all()
        supplier_info = []

        # Creare un modulo per ogni fornitore
        for supplier in suppliers:
            form = SupplierForm(instance=supplier)
            supplier_info.append({'supplier': supplier, 'form': form})

        # Aggiungere un modulo vuoto per la creazione di nuovi fornitori
        create_form = SupplierForm()

        return render(request, self.template_name, {
            'supplier_info': supplier_info,
            'create_form': create_form,
        })

    def post(self, request, *args, **kwargs):
        if 'create_supplier' in request.POST:
            supplier_form = SupplierForm(request.POST)
            if supplier_form.is_valid():
                supplier_form.save()
                messages.success(request, 'Fornitore creato con successo.')
                return redirect('crm:supplier_view')
            else:
                for field, errors in supplier_form.errors.items():
                    for error in errors:
                        messages.error(request, f"Errore nel campo '{field}': {error}")
        
        elif 'update_supplier' in request.POST:
            supplier_id = request.POST.get('supplier_id')
            supplier = get_object_or_404(Supplier, id=supplier_id)
            supplier_form = SupplierForm(request.POST, instance=supplier)
            if supplier_form.is_valid():
                supplier_form.save()
                messages.success(request, 'Fornitore aggiornato con successo.')
                return redirect('crm:supplier_view')
            else:
                for field, errors in supplier_form.errors.items():
                    for error in errors:
                        messages.error(request, f"Errore nel campo '{field}': {error}")
        
        elif 'delete_supplier' in request.POST:
            supplier_id = request.POST.get('supplier_id')
            supplier = get_object_or_404(Supplier, id=supplier_id)
            supplier.delete()
            messages.success(request, 'Fornitore eliminato con successo.')
            return redirect('crm:supplier_view')
        
        # Se si arriva qui, non è stato fatto nulla di valido
        suppliers = Supplier.objects.all()
        supplier_info = []

        for supplier in suppliers:
            form = SupplierForm(instance=supplier)
            supplier_info.append({'supplier': supplier, 'form': form})

        create_form = SupplierForm()

        return render(request, self.template_name, {
            'supplier_info': supplier_info,
            'create_form': create_form,
        })

class CustomerView(LoginRequiredMixin, View):
    template_name = 'crm/customer.html'
    
    def get(self, request, *args, **kwargs):
        customers = Customer.objects.all()
        customer_info = []

        # Creare un modulo per ogni cliente
        for customer in customers:
            form = CustomerForm(instance=customer)
            customer_info.append({'customer': customer, 'form': form})

        # Aggiungere un modulo vuoto per la creazione di nuovi clienti
        create_form = CustomerForm()

        return render(request, self.template_name, {
            'customer_info': customer_info,
            'create_form': create_form,
        })

    def post(self, request, *args, **kwargs):
        if 'create_customer' in request.POST:
            customer_form = CustomerForm(request.POST)
            if customer_form.is_valid():
                customer_form.save()
                messages.success(request, 'Cliente creato con successo.')
                return redirect('crm:customer_view')
            else:
                for field, errors in customer_form.errors.items():
                    for error in errors:
                        messages.error(request, f"Errore nel campo '{field}': {error}")
        
        elif 'update_customer' in request.POST:
            customer_id = request.POST.get('customer_id')
            customer = get_object_or_404(Customer, id=customer_id)
            customer_form = CustomerForm(request.POST, instance=customer)
            if customer_form.is_valid():
                customer_form.save()
                messages.success(request, 'Cliente aggiornato con successo.')
                return redirect('crm:customer_view')
            else:
                for field, errors in customer_form.errors.items():
                    for error in errors:
                        messages.error(request, f"Errore nel campo '{field}': {error}")
        
        elif 'delete_customer' in request.POST:
            customer_id = request.POST.get('customer_id')
            customer = get_object_or_404(Customer, id=customer_id)
            customer.delete()
            messages.success(request, 'Cliente eliminato con successo.')
            return redirect('crm:customer_view')
        
        # Se si arriva qui, non è stato fatto nulla di valido
        customers = Customer.objects.all()
        customer_info = []

        for customer in customers:
            form = CustomerForm(instance=customer)
            customer_info.append({'customer': customer, 'form': form})

        create_form = CustomerForm()

        return render(request, self.template_name, {
            'customer_info': customer_info,
            'create_form': create_form,
        })
