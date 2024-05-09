from django.db import models

from backend.clinicaSaude.clinicaSaudeApp.models import fk
from backend.clinicaSaude.clinicaSaudeApp.models.user import User
from backend.clinicaSaude.clinicaSaudeApp.models.doctor import Doctor


class Appointment(models.Model):

    patient = fk(User)
    doctor = fk(Doctor)
    specialty = models.CharField(max_length=255)
    date = models.DateTimeField()
    is_confirmed = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)


