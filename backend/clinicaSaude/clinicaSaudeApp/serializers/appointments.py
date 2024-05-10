from rest_framework import serializers
from .user import GetUsername, GetDoctor, GetAllDoctors, GetUserAll, GetUser
from clinicaSaudeApp.models import Appointment


class GetAllAppointments(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ["id", "patient", "doctor"]


class GetAppointment(serializers.ModelSerializer):
    doctor = GetDoctor(read_only=True)
    patient = GetUser(read_only=True)

    class Meta:
        model = Appointment
        fields = ["id", "patient", "doctor", "specialty", "date"]
