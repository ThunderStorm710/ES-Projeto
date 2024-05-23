import os

from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from . import auxDoctor
from .auxFunctions.compare_faces import compare_faces
from .auxFunctions.index_faces import index_faces
from .auxFunctions.search_faces import search_faces_by_image
from django.conf import settings
from clinicaSaudeApp.models import AuthUser, User, Doctor, Appointment, TimeSlot, Payment


# @login_required()
@api_view(["POST"])
def index_face_view(request):
    user_id = request.POST.get('userId')
    print(user_id)
    if 'patient_id' not in request.POST or request.POST.get('patient_id') == -1:
        user = User.objects.filter(user__username=request.user).first()
        if not user:
            return JsonResponse({'error': 'User not found'}, status=400)
        patient_id = user.id
    else:
        patient_id = request.data.get('patient_id')

    if request.method == 'POST' and 'image' in request.FILES:
        image = request.FILES['image']
        save_path = os.path.join(settings.MEDIA_ROOT, image.name)
        path = default_storage.save(save_path, image)
        index_faces(save_path, patient_id)
        return JsonResponse({'url': f"{settings.MEDIA_URL}{image.name}"})
    return JsonResponse({'error': 'Invalid request or missing image file'}, status=400)



# @login_required()
@api_view(["POST"])
def search_face_view(request):
    print(request.POST)
    print(request.data)
    print(request.FILES)

    if 'patient_id' not in request.POST or request.POST.get('patient_id') == -1:
        user = User.objects.filter(user__username=request.user).first()
        if not user:
            print("NOT FOUND")
            return JsonResponse({'error': 'User not found'}, status=400)
        patient_id = user.id
    else:
        patient_id = request.data.get('patient_id')

    print(patient_id)

    if request.method == 'POST' and 'image' in request.FILES:
        image = request.FILES['image']
        save_path = os.path.join(settings.MEDIA_ROOT, image.name)
        path = default_storage.save(save_path, image)
        result = search_faces_by_image(save_path)
        print(result)

        if str(result) == str(patient_id):
            print("IGUAIS")
            return JsonResponse({'match': True, "mensagem": "Encontrado"}, status=200)
        else:
            print("DIFERENTES")
            return JsonResponse({'match': False, "mensagem": "Não encontrado"}, status=200)

    return JsonResponse({'error': 'Invalid request or missing image file', 'match': False}, status=400)


@api_view(["GET"])
def compare_faces_view(request, id):
    appointment = Appointment.objects.filter(id=id, is_done=False, is_canceled=False)
    if not appointment:
        return JsonResponse(
            {"invalid": "Appointment does not exist", "message": False},
            status=status.HTTP_400_BAD_REQUEST,
        )
    appointment = appointment.first()

    if compare_faces():
        return JsonResponse(
            {"appointment_id": appointment.id, "id": appointment.patient.id, "doctor_id": appointment.doctor.id,
             "specialty": appointment.specialty.indicator})

    else:
        JsonResponse({"invalid": "Face ID: No match was found", "message": False},
                     status=status.HTTP_400_BAD_REQUEST,
                     )
