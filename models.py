# CRM models.py

from django.db import models
from django.utils.translation import gettext_lazy as _

class Company(models.Model):
    name = models.CharField(_("nome"), max_length=100)
    address = models.TextField(_("indirizzo"))

    class Meta:
        verbose_name = _("azienda")
        verbose_name_plural = _("aziende")

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(_("nome"), max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='suppliers', verbose_name=_("azienda"))
    email = models.EmailField(_("email"))
    phone = models.CharField(_("telefono"), max_length=20)

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
    ]
    
    name = models.CharField(_("nome"), max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='customers', verbose_name=_("azienda"))
    email = models.EmailField(_("email"))
    phone = models.CharField(_("telefono"), max_length=20)
    status = models.CharField(_("stato"), max_length=20, choices=STATUSES, default='LEAD')

    class Meta:
        verbose_name = _("cliente")
        verbose_name_plural = _("clienti")

    def __str__(self):
        return f"{self.name} - {self.company.name}"
