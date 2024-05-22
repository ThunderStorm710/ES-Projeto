from datetime import datetime
from django.contrib.auth.decorators import login_required
from clinicaSaudeApp.models import AuthUser, User, Doctor, Appointment, TimeSlot, Payment
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from clinicaSaudeApp.serializers import GetAllInfoAppointment
from . import auxDoctor
from . import auxSpecialty
import os
from django.conf import settings
from django.core.files.storage import default_storage
from .auxFunctions.compare_faces import compare_faces

from .auxFunctions.state_machine import state_machine


@api_view(["POST"])
def create_appointment_view(request):

    if "slot_id" not in request.data or "doctor_id" not in request.data or "value" not in request.data:
        return JsonResponse(
            {"invalid": "Missing parameters", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if "patient_id" not in request.data or request.data.get("patient_id") == -1:
        user = User.objects.filter(user__username=request.user).first()
        print(user.id, "_---")
        patient_id = user.id
    else:
        patient_id = request.data.get("patient_id")

    print(request.data)
    slot_id = request.data.get("slot_id")
    doctor_id = request.data.get("doctor_id")
    value = request.data.get("value")

    patient = User.objects.filter(id=patient_id).first()

    if not patient:
        return JsonResponse(
            {"invalid": "Patient does not exist", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )

    doctor = auxDoctor.getDoctorById(str(doctor_id))
    if doctor is None:
        return JsonResponse(
            {"invalid": "Doctor does not exist", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )

    slot = TimeSlot.objects.filter(id=slot_id).first()

    if not slot:
        return JsonResponse(
            {"invalid": "Slot does not exist", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )
    if slot is not None and not slot.is_available:
        return JsonResponse(
            {"invalid": "Slot is unavailable", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )
    '''
    appointment_exists = Appointment.objects.filter(patient=patient, doctor_id=doctor_id, slot=slot).exists()

    if appointment_exists:
        return JsonResponse(
            {"invalid": "Appointment already exists", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )
    '''
    appointment = Appointment.objects.create(
        patient=patient, doctor_id=doctor_id, value=value, slot=slot
    )

    appointment.save()

    slot.is_available = False

    slot.save()

    payment = Payment.objects.create(appointment=appointment, patient=patient, value=value, date=datetime.now())

    payment.save()

    state_machine({"appointment_id": appointment.id, "payment_id": payment.id})

    print({"id": appointment.id, "message": True})
    return JsonResponse({"id": appointment.id, "message": True})


# @login_required()
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
        {"appointment_id": appointment.id, "id": appointment.patient.id, "doctor_id": appointment.doctor_id,
         "value": appointment.value})



@api_view(["GET"])
def get_appointment_by_patient_id_view(request):
    if "patient_id" not in request.data or request.data.get("patient_id") == -1:
        user = User.objects.filter(user__username=request.user).first()
        patient_id = user.id
        appointment = Appointment.objects.filter(patient=user)

    else:
        patient_id = request.data.get("patient_id")
        appointment = Appointment.objects.filter(patient_id=patient_id)


    if not appointment:
        return JsonResponse(
            {"invalid": "Appointments do not exist", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )

    response = []
    for p in appointment:
        slot = p.slot
        doctor = auxDoctor.getDoctorById(slot.doctor_id)
        print(doctor, "------------_")
        specialty = auxSpecialty.getSpecialtiesById(doctor['specialty_id'])
        response.append(
            {"id": p.id, "patient": p.patient.id, "date": slot.date, "start_time": slot.start_time, "specialty": specialty['name'], "doctor": doctor['name'],
             "value": p.value, "is_finished": p.is_finished, "is_scheduled": p.is_scheduled}
        )

    print(response)

    return JsonResponse(
        {"appointments": response})





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


@api_view(["POST"])
def finish_appointment_view(request):
    if "appointment_id" not in request.data:
        return JsonResponse(
            {"invalid": "Missing parameters", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )
    appointment_id = request.data.get("appointment_id")
    if "patient_id" not in request.data or request.data.get("patient_id") == -1:
        user = User.objects.filter(user__username=request.user).first()
        patient_id = user.id
    else:
        patient_id = request.data.get("patient_id")


    appointments = Appointment.objects.filter(id=appointment_id, patient_id=patient_id)
    if not appointments:
        return JsonResponse(
            {"error": "No appointments found", "message": False},
            status=status.HTTP_404_NOT_FOUND,
        )
    appointment = appointments.first()
    appointment.is_finished = True
    appointment.save()
    return JsonResponse(
        {"message": "Appointment finished", "id": appointment.id, "is_finished": appointment.is_finished}
    )


@api_view(["POST"])
def upload_image(request):
    if request.method == 'POST' and 'image' in request.FILES:
        image = request.FILES['image']
        save_path = os.path.join(settings.MEDIA_ROOT, image.name)
        path = default_storage.save(save_path, image)
        # search_faces_by_image(image.name)
        compare_faces(save_path)
        return JsonResponse({'url': f"{settings.MEDIA_URL}{image.name}"})
    return JsonResponse({'error': 'Invalid request or missing image file'}, status=400)
