from django.core.validators import MinValueValidator
from django.db import models


class TimeSlot(models.Model):
    doctor_id = models.IntegerField(validators=[MinValueValidator(1)])
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)
