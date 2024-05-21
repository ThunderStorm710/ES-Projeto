from datetime import datetime
from django.contrib.auth.decorators import login_required
from clinicaSaudeApp.models import AuthUser, User, Doctor, Appointment, Payment, Specialty
from django.http import HttpResponseBadRequest, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from clinicaSaudeApp.serializers import GetSpecialty
import boto3

from . import auxSpecialty
from .auxFunctions.populate_slot import populate_time_slots


# @login_required()
@api_view(["POST"])
def create_specialty_view(request):
    '''
    id = request.data.get("indicator")

    specialty = Specialty.objects.filter(indicator=id).exists()

    if specialty:
        return JsonResponse(
            {"invalid": "Specialty already exists", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )

    specialty = Specialty.objects.create(indicator=id)

    specialty.save()
    '''
    #populate_time_slots(doctor_id=1, date='2024-05-18', start_hour=9, end_hour=17)
    id, message = auxSpecialty.insertSpecialty(request.data)

    if id != -1:
        return JsonResponse({"id": id, "message": True})
    else:
        return JsonResponse(
            {"invalid": message, "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )

# @login_required()
@api_view(["GET"])
def get_all_specialties_view(request):
    try:
        '''
        specialties = Specialty.objects.all()
        print(specialties)
        if not specialties:
            return JsonResponse(
                {"error": "No specialties found", "message": False},
                status=status.HTTP_404_NOT_FOUND,
            )
        specialties = GetSpecialty(specialties, many=True).data
        return JsonResponse(specialties, safe=False)
        '''
        data = auxSpecialty.getAllSpecialties()
        data.sort(key=lambda x: x['SpecialtyId'])
        #populate_time_slots(doctor_id=1, date='2024-05-18', start_hour=9, end_hour=17)
        return JsonResponse(data, safe=False)

    except Exception as e:
        return JsonResponse(
            {"error": str(e), "message": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
