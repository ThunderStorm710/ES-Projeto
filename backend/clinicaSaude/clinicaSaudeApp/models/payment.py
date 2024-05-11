from django.db import models
from . import fk
from .user import User
from .doctor import Doctor
from .appointment import Appointment


class Payment(models.Model):

    appointment = fk(Appointment)
    patient = fk(User)
    value = models.FloatField()
    date = models.DateTimeField()


