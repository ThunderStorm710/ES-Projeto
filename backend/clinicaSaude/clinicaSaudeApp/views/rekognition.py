from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from . import auxDoctor


#@login_required()
@api_view(["POST"])
def index_face_view(request):


    if not patient:
        return JsonResponse(
            {"invalid": "Patient does not exist", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )

    doctor = auxDoctor.getDoctorsById(str(doctor_id))
    if doctor is None:
        return JsonResponse(
            {"invalid": "Doctor does not exist", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )

    print(doctor)

    appointment_exists = Appointment.objects.filter(patient=patient, doctor=doctor, specialty=doctor.specialty, date=date).exists()

    if appointment_exists:
        return JsonResponse(
            {"invalid": "Appointment already exists", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )

    appointment = Appointment.objects.create(
        patient=patient, doctor=doctor, specialty=doctor.specialty, date=date, value=value
    )

    appointment.save()

    return JsonResponse({"id": appointment.id, "message": True})

#@login_required()
@api_view(["GET"])
def search_face_view(request, id):
    appointment = Appointment.objects.filter(id=id)
    if not appointment:
        return JsonResponse(
            {"invalid": "Appointment does not exist", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )
    appointment = appointment.first()
    return JsonResponse(
        {"appointment_id": appointment.id, "id": appointment.patient.id, "doctor_id": appointment.doctor.id, "specialty": appointment.specialty.indicator})