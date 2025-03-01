from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from crm.models import Company, Person, CompanyCategory
from crm.forms import CompanyForm, PersonForm, CompanyCategoryForm

class CompanyListView(View):
    template_name = 'crm/companies.html'

    def get(self, request, *args, **kwargs):
        companies = Company.objects.all()
        form = CompanyForm()
        return render(request, self.template_name, {'companies': companies, 'form': form})

    def post(self, request, *args, **kwargs):
        if 'delete_object' in request.POST:
            company = get_object_or_404(Company, id=request.POST.get('delete_object'))
            company.delete()
            return redirect('crm:company_list')

        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crm:company_list')

        companies = Company.objects.all()
        return render(request, self.template_name, {'companies': companies, 'form': form})

class CompanyDetailView(View):
    template_name = 'crm/company_detail.html'

    def get(self, request, company_id, *args, **kwargs):
        company = get_object_or_404(Company, id=company_id)
        form = CompanyForm(instance=company)
        return render(request, self.template_name, {'company': company, 'form': form})

    def post(self, request, company_id, *args, **kwargs):
        company = get_object_or_404(Company, id=company_id)

        if 'update_company' in request.POST:
            form = CompanyForm(request.POST, instance=company)
            if form.is_valid():
                form.save()
                return redirect('crm:company_list')

        elif 'delete_company' in request.POST:
            company.delete()
            return redirect('crm:company_list')

        return render(request, self.template_name, {'company': company, 'form': form})

class PersonListView(View):
    template_name = 'crm/people.html'

    def get(self, request, *args, **kwargs):
        people = Person.objects.all()
        form = PersonForm()
        return render(request, self.template_name, {'people': people, 'form': form})

    def post(self, request, *args, **kwargs):
        if 'delete_object' in request.POST:
            person = get_object_or_404(Person, id=request.POST.get('delete_object'))
            person.delete()
            return redirect('crm:person_list')

        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crm:person_list')

        people = Person.objects.all()
        return render(request, self.template_name, {'people': people, 'form': form})

class PersonDetailView(View):
    template_name = 'crm/person_detail.html'

    def get(self, request, person_id, *args, **kwargs):
        person = get_object_or_404(Person, id=person_id)
        form = PersonForm(instance=person)
        return render(request, self.template_name, {'person': person, 'form': form})

    def post(self, request, person_id, *args, **kwargs):
        person = get_object_or_404(Person, id=person_id)

        if 'update_person' in request.POST:
            form = PersonForm(request.POST, instance=person)
            if form.is_valid():
                form.save()
                return redirect('crm:person_list')

        elif 'delete_person' in request.POST:
            person.delete()
            return redirect('crm:person_list')

        return render(request, self.template_name, {'person': person, 'form': form})

class CompanyCategoryListView(View):
    template_name = 'crm/categories.html'

    def get(self, request, *args, **kwargs):
        categories = CompanyCategory.objects.all()
        form = CompanyCategoryForm()
        return render(request, self.template_name, {'categories': categories, 'form': form})

    def post(self, request, *args, **kwargs):
        if 'delete_object' in request.POST:
            category = get_object_or_404(CompanyCategory, id=request.POST.get('delete_object'))
            category.delete()
            return redirect('crm:category_list')

        form = CompanyCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crm:category_list')

        categories = CompanyCategory.objects.all()
        return render(request, self.template_name, {'categories': categories, 'form': form})

class CompanyCategoryDetailView(View):
    template_name = 'crm/category_detail.html'

    def get(self, request, category_id, *args, **kwargs):
        category = get_object_or_404(CompanyCategory, id=category_id)
        form = CompanyCategoryForm(instance=category)
        return render(request, self.template_name, {'category': category, 'form': form})

    def post(self, request, category_id, *args, **kwargs):
        category = get_object_or_404(CompanyCategory, id=category_id)

        if 'update_category' in request.POST:
            form = CompanyCategoryForm(request.POST, instance=category)
            if form.is_valid():
                form.save()
                return redirect('crm:category_list')

        elif 'delete_category' in request.POST:
            category.delete()
            return redirect('crm:category_list')

        return render(request, self.template_name, {'category': category, 'form': form})
