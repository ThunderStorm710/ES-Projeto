from rest_framework import serializers
from .user import GetAllInfoUser, GetUser
from clinicaSaudeApp.models import Appointment


class GetAllInfoAppointment(serializers.ModelSerializer):
    patient = GetUser(read_only=True)

    class Meta:
        model = Appointment
        fields = ["id", "patient", "doctor_id", "slot"]
