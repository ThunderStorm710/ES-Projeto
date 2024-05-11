from rest_framework import serializers
from .appointments import GetUser, GetAllInfoAppointment
from clinicaSaudeApp.models import Appointment, Payment


class GetAllInfoPayment(serializers.ModelSerializer):
    patient = GetUser(read_only=True)
    appointment = GetAllInfoAppointment(read_only=True)

    class Meta:
        model = Payment
        fields = ["id", "patient", "appointment", "value", "date"]
