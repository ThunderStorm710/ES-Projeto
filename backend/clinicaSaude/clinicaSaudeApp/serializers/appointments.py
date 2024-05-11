from rest_framework import serializers
from .user import GetAllInfoUser, GetUser, GetDoctorInfo
from clinicaSaudeApp.models import Appointment


class GetAllInfoAppointment(serializers.ModelSerializer):
    doctor = GetDoctorInfo(read_only=True)
    patient = GetUser(read_only=True)

    class Meta:
        model = Appointment
        fields = ["id", "patient", "doctor", "specialty", "date"]
