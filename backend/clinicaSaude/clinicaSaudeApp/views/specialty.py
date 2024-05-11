from datetime import datetime
from django.contrib.auth.decorators import login_required
from clinicaSaudeApp.models import AuthUser, User, Doctor, Appointment, Payment, Specialty
from django.http import HttpResponseBadRequest, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from clinicaSaudeApp.serializers import GetSpecialty


#@login_required()
@api_view(["POST"])
def create_specialty_view(request):
    id = request.data.get("indicator")

    specialty = Specialty.objects.filter(indicator=id).exists()

    if specialty:
        return JsonResponse(
            {"invalid": "Specialty already exists", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )

    specialty = Specialty.objects.create(indicator=id)

    specialty.save()

    return JsonResponse({"id": specialty.id, "message": True})

#@login_required()
@api_view(["GET"])
def get_all_specialties_view(request):
    try:
        specialties = Specialty.objects.all()
        print(specialties)
        if not specialties:
            return JsonResponse(
                {"error": "No specialties found", "message": False},
                status=status.HTTP_404_NOT_FOUND,
            )
        specialties = GetSpecialty(specialties, many=True).data
        return JsonResponse(specialties, safe=False)
    except Exception as e:
        return JsonResponse(
            {"error": str(e), "message": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
