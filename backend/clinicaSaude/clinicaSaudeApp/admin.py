from django.contrib import admin

from .models import User, Appointment, TimeSlot, Payment

admin.site.register(User)
admin.site.register(Appointment)
admin.site.register(TimeSlot)
admin.site.register(Payment)

# Register your models here.
