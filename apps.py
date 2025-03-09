import logging
from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.db.utils import OperationalError, ProgrammingError

logger = logging.getLogger(__name__)

class CrmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm'

    def ready(self):
        post_migrate.connect(create_default_company, sender=self)

def create_default_company(sender, **kwargs):
    from .models.base import Company
    
    # Definizione dei dati dell'azienda predefinita
    default_company = {
        "name": "Horeca",
        "address": "Via Roma 123, Italia",
        "website": "https://www.horeca.it",
        "phone": "+39 123 456 7890",
        "email": "info@horeca.it",
        "notes": "Azienda principale del sistema",
        "is_own_company": True,
        "vat_number": "06967180487",
    }

    try:
        # Controlla se esiste già un'azienda contrassegnata come propria
        if not Company.objects.filter(is_own_company=True).exists():
            # Crea l'azienda predefinita se non ne esiste una propria
            Company.objects.create(**default_company)
            logger.info("Azienda principale creata con successo.")
    except (OperationalError, ProgrammingError) as e:
        # Logga un messaggio di errore se le tabelle non sono pronte o c'è un altro problema
        logger.error(
            "Impossibile creare l'azienda predefinita. "
            "Questo potrebbe essere dovuto alle tabelle non ancora pronte. "
            "Errore: %s", e
        )