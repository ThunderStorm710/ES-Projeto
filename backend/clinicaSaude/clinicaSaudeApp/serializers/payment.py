from rest_framework import serializers
from .user import GetUsername
from .appointments import GetAppointment
from clinicaSaudeApp.models import Appointment, Payment


class GetAllPayments(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["id", "patient", "doctor"]


class GetPayment(serializers.ModelSerializer):
    doctor = GetUsername(read_only=True)
    patient = GetUsername(read_only=True)
    appointment = GetAppointment(read_only=True)

    class Meta:
        model = Payment
        fields = ["id", "patient", "doctor", "value", "date", "is_paid"]
