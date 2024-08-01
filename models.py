# CRM models.py

from django.db import models
from django.utils.translation import gettext_lazy as _

class CompanyCategory(models.Model):
    name = models.CharField(_("nome"), max_length=100, db_index=True)
    description = models.TextField(_("descrizione"), blank=True)

    class Meta:
        verbose_name = _("categoria aziendale")
        verbose_name_plural = _("categorie aziendali")

    def __str__(self):
        return self.name

class Company(models.Model):
    STATUSES = [
        ('Supplier', _('Fornitore')),
        ('Customer', _('Cliente')),
    ]
    name = models.CharField(_("nome"), max_length=100, db_index=True)
    address = models.TextField(_("indirizzo"))
    category = models.ForeignKey(CompanyCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("categoria"))
    website = models.URLField(_("sito web"), blank=True)
    phone = models.CharField(_("telefono"), max_length=20, blank=True)
    email = models.EmailField(_("email"), blank=True)
    notes = models.TextField(_("note"), blank=True)
    type = models.CharField(_("tipologia"), max_length=20, choices=STATUSES, default='Supplier')
    class Meta:
        verbose_name = _("azienda")
        verbose_name_plural = _("aziende")

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(_("nome"), max_length=100, db_index=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='suppliers', verbose_name=_("azienda"))
    email = models.EmailField(_("email"))
    phone = models.CharField(_("telefono"), max_length=20)
    notes = models.TextField(_("note"), blank=True)

    class Meta:
        verbose_name = _("fornitore")
        verbose_name_plural = _("fornitori")

    def __str__(self):
        return f"{self.name} - {self.company.name}"

class Customer(models.Model):
    STATUSES = [
        ('LEAD', _('Lead')),
        ('ACTIVE', _('Cliente Attivo')),
        ('INACTIVE', _('Cliente Inattivo')),
        ('LOYAL', _('Cliente Fidelizzato')),
    ]
    
    name = models.CharField(_("nome"), max_length=100, db_index=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='customers', verbose_name=_("azienda"))
    email = models.EmailField(_("email"))
    phone = models.CharField(_("telefono"), max_length=20)
    status = models.CharField(_("stato"), max_length=20, choices=STATUSES, default='LEAD')

    class Meta:
        verbose_name = _("cliente")
        verbose_name_plural = _("clienti")

    def __str__(self):
        return f"{self.name} - {self.company.name}"
