from django.db import models
from . import fk
from .user import User
from .doctor import Doctor
from .appointment import Appointment


class Payment(models.Model):

    appointment = fk(Appointment)
    patient = fk(User)
    doctor = fk(Doctor)
    value = models.FloatField()
    date = models.DateTimeField()
    is_paid = models.BooleanField(default=False)


