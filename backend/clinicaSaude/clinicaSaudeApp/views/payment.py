from datetime import datetime
from django.contrib.auth.decorators import login_required
from clinicaSaudeApp.models import AuthUser, User, Doctor, Appointment, Payment
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from clinicaSaudeApp.serializers import GetAllInfoPayment

from . import auxDoctor, auxSpecialty


# @login_required()
@api_view(["POST"])
def create_payment_view(request):

    if "appointment_id" not in request.data or "patient_id" not in request.data or "value" not in request.data:
        print(1)
        return JsonResponse(
            {"invalid": "Missing parameters", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )
    print(1.1)
    if "patient_id" not in request.data or request.data.get("patient_id") == -1:
        user = User.objects.filter(user__username=request.user).first()
        patient_id = user.id
    else:
        patient_id = request.data.get("patient_id")

    print(2, patient_id)

    appointment_id = request.data.get("appointment_id")
    value = request.data.get("value")

    appointment = Appointment.objects.filter(id=appointment_id, value=value).first()
    payment = Payment.objects.filter(appointment_id=appointment_id, value=value)

    if not payment.exists():
        print(3)
        return JsonResponse(
            {"invalid": "Payment does not exist", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )

    patient = User.objects.filter(id=patient_id).first()
    print(patient)

    if not patient:
        print(4)
        return JsonResponse(
            {"invalid": "Patient does not exist", "message": False},
            status=status.HTTP_400_BAD_REQUEST)

    if appointment.patient.id != patient.id:
        print(5)
        return JsonResponse(
            {"invalid": "Patient does not match with appointment", "message": False},
            status=status.HTTP_400_BAD_REQUEST)

    payment = Payment.objects.filter(appointment=appointment, patient=patient, value=value).first()

    if not payment:
        print(6)
        return JsonResponse(
            {"invalid": "Payment not found", "message": False},
            status=status.HTTP_400_BAD_REQUEST)
    else:
        print(7)
        payment.is_done = True
        payment.is_canceled = False
        payment.date = datetime.now()
        payment.save()
        return JsonResponse(
            {"payment_id": payment.id, "patient_id": payment.patient.id, "appointment_id": payment.appointment.id,
             "value": payment.value, "is_done": payment.is_done, "is_canceled": payment.is_canceled,
             "date": payment.date})

    # payment = Payment.objects.create(appointment=appointment, patient=patient, value=value, date=datetime.now())
    # payment.save()

    #return JsonResponse({"id": payment.id, "message": True})


# @login_required()
@api_view(["GET"])
def get_payment_by_id_view(request, id):
    payment = Payment.objects.filter(id=id)
    if not payment:
        return JsonResponse(
            {"invalid": "Payment does not exist", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )
    payment = payment.first()
    slot = payment.appointment.slot
    doctor = auxDoctor.getDoctorById(slot.doctor_id)
    specialty = auxSpecialty.getSpecialtiesById(doctor['specialty_id'])

    return JsonResponse(
        {"payment_id": payment.id, "patient_id": payment.patient.id, "appointment_id": payment.appointment.id,
         "value": payment.value, "is_canceled": payment.is_canceled, "is_done": payment.is_done,
         "start_time": payment.appointment.slot.start_time, "date": payment.appointment.slot.date,
         "doctor": doctor['name'], "specialty": specialty['name']})


@api_view(["GET"])
def get_payment_by_patient_id_view(request):
    if "patient_id" not in request.data or request.data.get("patient_id") == -1:
        user = User.objects.filter(user__username=request.user).first()
        patient_id = user.id
    else:
        patient_id = request.data.get("patient_id")

    payment = Payment.objects.filter(patient_id=patient_id)

    if not payment:
        return JsonResponse(
            {"invalid": "Payments do not exist", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )

    response = []
    doctorList = []
    for p in payment:
        doctorList.append(p.appointment.slot.doctor_id)

    doctors = auxDoctor.getDoctorsByIds(doctorList)

    specialtyList = []

    for d in doctors:
        specialtyList.append(d['specialty_id'])

    specialties = auxSpecialty.getSpecialtiesByIds(specialtyList)

    for i in range(len(payment)):
        appointment = payment[i].appointment
        slot = appointment.slot
        doctor = doctors[i]
        specialty = specialties[i]
        response.append(
            {"id": payment[i].id, "patient": payment[i].patient.id, "date": slot.date, "start_time": slot.start_time,
             "specialty": specialty['name'], "doctor": doctor['name'],
             "value": payment[i].value, "is_done": payment[i].is_done, "is_canceled": payment[i].is_canceled}
        )
    '''
    for p in payment:
        appointment = Appointment.objects.filter(id=p.appointment.id).first()
        slot = appointment.slot
        doctor = auxDoctor.getDoctorById(slot.doctor_id)
        print(doctor, "------------_")
        specialty = auxSpecialty.getSpecialtiesById(doctor['specialty_id'])
        response.append(
            {"id": p.id, "patient": p.patient.id, "date": slot.date, "start_time": slot.start_time, "specialty": specialty['name'], "doctor": doctor['name'],
             "value": p.value, "is_done": p.is_done, "is_canceled": p.is_canceled}
        )
    '''

    #print(response)

    return JsonResponse(
        {"payments": response})


@api_view(["GET"])
def get_all_payments_view(request):
    try:
        payments = Payment.objects.all()
        #print(payments)
        if not payments:
            return JsonResponse(
                {"error": "No payments found", "message": False},
                status=status.HTTP_404_NOT_FOUND,
            )

        payments = GetAllInfoPayment(payments, many=True).data

        #print(payments)

        return JsonResponse(payments, safe=False)
    except Exception as e:
        return JsonResponse(
            {"error": str(e), "message": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
