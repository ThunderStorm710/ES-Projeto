from rest_framework import serializers
from clinicaSaudeApp.models import AuthUser, Doctor, User
from .specialty import GetSpecialty



class GetAllInfoUser(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ["username", "email"]

class GetUser(serializers.ModelSerializer):
    user = GetAllInfoUser(read_only=True)

    class Meta:
        model = User
        fields = ["user"]

class GetDoctorInfo(serializers.ModelSerializer):
    specialty = GetSpecialty(read_only=True)

    class Meta:
        model = Doctor
        fields = ["name", "email", "specialty"]




