from datetime import datetime
from django.contrib.auth.decorators import login_required
from clinicaSaudeApp.models import AuthUser, User, Doctor, Appointment
from django.http import HttpResponseBadRequest, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from clinicaSaudeApp.serializers import GetAllInfoAppointment



#@login_required()
@api_view(["POST"])
def create_appointment_view(request):
    print(request.data)
    patient_id = request.data.get("patient_id")
    doctor_id = request.data.get("doctor_id")
    date = request.data.get("date")
    value = request.data.get("value")
    date = datetime.strptime(date, "%d/%m/%Y")


    patient = User.objects.filter(id=patient_id).first()
    doctor = Doctor.objects.filter(id=doctor_id).first()

    if not patient or not doctor:
        return JsonResponse(
            {"invalid": "Patient or Doctor does not exist", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )

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
def get_appointment_by_id_view(request, id):
    appointment = Appointment.objects.filter(id=id)
    if not appointment:
        return JsonResponse(
            {"invalid": "Appointment does not exist", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )
    appointment = appointment.first()
    return JsonResponse(
        {"appointment_id": appointment.id, "id": appointment.patient.id, "doctor_id": appointment.doctor.id, "specialty": appointment.specialty.indicator})

@api_view(["GET"])
def get_all_appointments_view(request):
    try:
        appointments = Appointment.objects.all()
        if not appointments:
            return JsonResponse(
                {"error": "No appointments found", "message": False},
                status=status.HTTP_404_NOT_FOUND,
            )

        appointments = GetAllInfoAppointment(appointments, many=True).data

        return JsonResponse(appointments, safe=False)
    except Exception as e:
        return JsonResponse(
            {"error": str(e), "message": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
