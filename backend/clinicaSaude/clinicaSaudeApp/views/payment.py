from datetime import datetime
from django.contrib.auth.decorators import login_required
from clinicaSaudeApp.models import AuthUser, User, Doctor, Appointment, Payment
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from clinicaSaudeApp.serializers import GetAllInfoPayment


# @login_required()
@api_view(["POST"])
def create_payment_view(request):
    appointment_id = request.data.get("appointment_id")
    patient_id = request.data.get("patient_id")
    value = request.data.get("value")

    appointment = Appointment.objects.filter(id=appointment_id, value=value).first()
    payment = Payment.objects.filter(id=appointment_id, value=value)

    if not payment.exists():
        return JsonResponse(
            {"invalid": "Payment does not exist", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )

    patient = User.objects.filter(id=patient_id).first()
    print(appointment)
    print(patient)

    if not patient:
        return JsonResponse(
            {"invalid": "Patient does not exist", "message": False},
            status=status.HTTP_400_BAD_REQUEST)

    if appointment.patient.id != patient.id:
        return JsonResponse(
            {"invalid": "Patient does not match with appointment", "message": False},
            status=status.HTTP_400_BAD_REQUEST)

    payment = Payment.objects.filter(appointment=appointment, patient=patient, value=value).first()

    if not payment:
        return JsonResponse(
            {"invalid": "Payment not found", "message": False},
            status=status.HTTP_400_BAD_REQUEST)
    else:
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

    return JsonResponse({"id": payment.id, "message": True})


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
    return JsonResponse(
        {"payment_id": payment.id, "patient_id": payment.patient.id, "appointment_id": payment.appointment.id,
         "value": payment.value})


@api_view(["GET"])
def get_all_payments_view(request):
    try:
        payments = Payment.objects.all()
        print(payments)
        if not payments:
            return JsonResponse(
                {"error": "No payments found", "message": False},
                status=status.HTTP_404_NOT_FOUND,
            )

        payments = GetAllInfoPayment(payments, many=True).data

        print(payments)

        return JsonResponse(payments, safe=False)
    except Exception as e:
        return JsonResponse(
            {"error": str(e), "message": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
