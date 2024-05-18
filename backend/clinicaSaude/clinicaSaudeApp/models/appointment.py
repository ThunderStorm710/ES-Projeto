from django.core.validators import MinValueValidator
from django.db import models

from . import fk
from .user import User
from .doctor import Doctor
from .specialty import Specialty
from .slot import TimeSlot


class Appointment(models.Model):

    slot = models.OneToOneField(TimeSlot, on_delete=models.CASCADE)
    patient = fk(User)
    doctor_id = models.IntegerField(validators=[MinValueValidator(1)])
    value = models.FloatField()
    is_scheduled = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)


