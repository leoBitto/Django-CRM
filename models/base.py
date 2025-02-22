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
    name = models.CharField(_("nome"), max_length=100, db_index=True)
    address = models.CharField(_("indirizzo"), max_length=200)
    category = models.ForeignKey(CompanyCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("categoria"))
    website = models.URLField(_("sito web"), blank=True)
    phone = models.CharField(_("telefono"), max_length=20, blank=True)
    email = models.EmailField(_("email"), blank=True)
    notes = models.TextField(_("note"), blank=True)
    is_own_company = models.BooleanField(_("azienda propria"), default=False)

    class Meta:
        verbose_name = _("azienda")
        verbose_name_plural = _("aziende")

    def __str__(self):
        return self.name

class Person(models.Model):
    ROLES = [
        ('PRIMARY', _('Contatto Principale')),
        ('PURCHASING', _('Responsabile Acquisti')),
        ('SALES', _('Responsabile Vendite')),
        ('OTHER', _('Altro')),
    ]

    first_name = models.CharField(_("nome"), max_length=50)
    last_name = models.CharField(_("cognome"), max_length=50)
    email = models.EmailField(_("email"))
    phone = models.CharField(_("telefono"), max_length=20)
    role = models.CharField(_("ruolo"), max_length=20, choices=ROLES, default='OTHER')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='contacts', verbose_name=_("azienda"))

    class Meta:
        verbose_name = _("persona di riferimento")
        verbose_name_plural = _("persone di riferimento")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.company.name}"
