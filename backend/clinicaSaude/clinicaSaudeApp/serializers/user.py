from rest_framework import serializers

from clinicaSaudeApp.models import AuthUser, Doctor, User


class GetUserAll(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ["username", "email", "password"]


class GetUsername(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ["username"]


class GetDoctor(serializers.ModelSerializer):
    user = GetUserAll(read_only=True)

    class Meta:
        model = User
        fields = ["user"]


class GetAllDoctors(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["id", "name", "specialty"]


class GetUser(serializers.ModelSerializer):
    user = GetUserAll(read_only=True)

    class Meta:
        model = User
        fields = ["user"]

