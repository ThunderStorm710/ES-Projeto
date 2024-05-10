from django.db import models

from . import fk
from .user import User
from .doctor import Doctor


class Appointment(models.Model):

    patient = fk(User)
    doctor = fk(Doctor)
    specialty = models.CharField(max_length=255)
    date = models.DateTimeField()


