from django.db import models

from . import fk
from .user import User
from .doctor import Doctor
from .specialty import Specialty


class Appointment(models.Model):

    patient = fk(User)
    doctor = fk(Doctor)
    value = models.FloatField()
    specialty = fk(Specialty)
    date = models.DateTimeField()


