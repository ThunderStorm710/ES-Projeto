from django.contrib.auth.decorators import login_required
from clinicaSaudeApp.models import AuthUser, User, Doctor, Specialty
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from clinicaSaudeApp.serializers import GetDoctorInfo
from . import auxDoctor


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
    '''
    name = request.data.get("name")
    email = request.data.get("email")
    specialty = request.data.get("specialty")

    doctor_already_exists = Doctor.objects.filter(email=email, name=name).exists()

    if doctor_already_exists:
        return JsonResponse(
            {"invalid": "Doctor already exists", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )

    specialty = Specialty.objects.filter(indicator=specialty)

    if not specialty:
        return JsonResponse(
            {"invalid": "Undefined specialty", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )
    specialty = specialty.first()

    doctor = Doctor.objects.create(
        name=name, email=email, specialty=specialty
    )

    doctor.save()
    '''
    id, message = auxDoctor.insertDoctor(request.data)

    if id != -1:
        return JsonResponse({"id": id, "message": True})
    else:
        return JsonResponse(
            {"invalid": message, "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
def get_doctors_view(request):
    '''
    doctors = Doctor.objects.all()
    if not doctors:
        return JsonResponse(
            {"invalid": "No doctors registered", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )
    doctors_ids = [doctor.id for doctor in doctors]
    '''
    data = auxDoctor.getAllDoctors()
    doctors_ids = []
    if data is None:
        return JsonResponse(
            {"invalid": "No doctors registered", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )
    for i in data:
        doctors_ids.append(i['DoctorId'])

    return JsonResponse({"doctor_ids": doctors_ids})


@api_view(["GET"])
def get_users_view(request):
    users = User.objects.all()
    if not users:
        return JsonResponse(
            {"invalid": "No users registered", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )
    user_ids = [user.id for user in users]
    return JsonResponse({"user_ids": user_ids})


@api_view(["GET"])
def get_doctor_by_id_view(request, id):
    '''
    doctor = Doctor.objects.filter(id=id)
    if not doctor:
        return JsonResponse(
            {"invalid": "Doctor does not exist", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )
    doctor = doctor.first()
    doctor = GetDoctorInfo(doctor).data
    '''

    doctor = auxDoctor.getDoctorsById(str(id))
    if doctor is None:
        return JsonResponse(
            {"invalid": "Doctor does not exist", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )

    return JsonResponse({"doctor": doctor})
