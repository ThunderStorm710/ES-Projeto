from django.contrib.auth.decorators import login_required
from clinicaSaudeApp.models import AuthUser, User, Doctor
from django.shortcuts import get_object_or_404

from django.http import HttpResponseBadRequest, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(["POST"])
def register_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")

    user_already_exists = AuthUser.objects.filter(username=username).exists()

    if user_already_exists:
        return JsonResponse(
            {"invalid": "User already exists", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )

    user_already_exists = AuthUser.objects.filter(email=email).exists()

    if user_already_exists:
        return JsonResponse(
            {"invalid": "Email already used", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )

    auth_user = AuthUser.objects.create_user(
        username=username, password=password, email=email
    )

    user = User.objects.create(user=auth_user)
    user.save()

    return JsonResponse({"id": user.id, "message": True})


@api_view(["POST"])
def create_doctor_view(request):
    name = request.data.get("name")
    email = request.data.get("email")
    specialty = request.data.get("specialty")

    doctor_already_exists = Doctor.objects.filter(email=email).exists()

    if doctor_already_exists:
        return JsonResponse(
            {"invalid": "Doctor already exists", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )

    doctor = Doctor.objects.create(
        name=name, email=email, specialty=specialty
    )

    doctor.save()

    return JsonResponse({"id": doctor.id, "message": True})


@api_view(["GET"])
def get_doctors_view(request):
    doctors = Doctor.objects.all()
    if not doctors:
        return JsonResponse(
            {"invalid": "No doctors registered", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )
    doctors_ids = [doctor.id for doctor in doctors]
    return JsonResponse({"doctor_ids": doctors_ids})


@api_view(["GET"])
def get_doctor_by_id_view(request, id):
    doctor = Doctor.objects.filter(id=id)
    if not doctor:
        return JsonResponse(
            {"invalid": "Doctor does not exist", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )
    doctor = doctor.first()
    return JsonResponse({"doctor_id": doctor.id, "name": doctor.name, "email": doctor.email, "specialty": doctor.specialty})