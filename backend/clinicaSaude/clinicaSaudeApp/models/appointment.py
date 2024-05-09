from django.db import models

from backend.clinicaSaude.clinicaSaudeApp.models import fk
from backend.clinicaSaude.clinicaSaudeApp.models.user import User


class Appointment(models.Model):

    type = models.CharField(max_length=255)
    patient = fk(User)
    doctor = fk(User)
    date = models.DateTimeField()
    description = models.TextField()
    is_confirmed = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)


