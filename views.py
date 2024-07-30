from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy
from .models import Company, Supplier, Customer
from .forms import CompanyForm, SupplierForm, CustomerForm

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
                return redirect('crm:company_view')
        
        elif 'update_company' in request.POST:
            company_id = request.POST.get('company_id')
            company = get_object_or_404(Company, id=company_id)
            company_form = CompanyForm(request.POST, instance=company)
            if company_form.is_valid():
                company_form.save()
                return redirect('crm:company_view')
        
        elif 'delete_company' in request.POST:
            company_id = request.POST.get('company_id')
            company = get_object_or_404(Company, id=company_id)
            company.delete()
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
                return redirect('crm:supplier_view')
        
        elif 'update_supplier' in request.POST:
            supplier_id = request.POST.get('supplier_id')
            supplier = get_object_or_404(Supplier, id=supplier_id)
            supplier_form = SupplierForm(request.POST, instance=supplier)
            if supplier_form.is_valid():
                supplier_form.save()
                return redirect('crm:supplier_view')
        
        elif 'delete_supplier' in request.POST:
            supplier_id = request.POST.get('supplier_id')
            supplier = get_object_or_404(Supplier, id=supplier_id)
            supplier.delete()
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
                return redirect('crm:customer_view')
        
        elif 'update_customer' in request.POST:
            customer_id = request.POST.get('customer_id')
            customer = get_object_or_404(Customer, id=customer_id)
            customer_form = CustomerForm(request.POST, instance=customer)
            if customer_form.is_valid():
                customer_form.save()
                return redirect('crm:customer_view')
        
        elif 'delete_customer' in request.POST:
            customer_id = request.POST.get('customer_id')
            customer = get_object_or_404(Customer, id=customer_id)
            customer.delete()
            return redirect('crm:customer_view')
        
        customers = Customer.objects.all()
        return render(request, self.template_name, {
            'customers': customers,
            'customer_form': customer_form,
        })
