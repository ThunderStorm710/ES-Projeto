from django.db import models

from backend.clinicaSaude.clinicaSaudeApp.models import fk
from backend.clinicaSaude.clinicaSaudeApp.models.user import User


class Payment(models.Model):

    patient = fk(User)
    doctor = fk(User)
    value = models.FloatField()
    date = models.DateTimeField()
    is_paid = models.BooleanField(default=False)

