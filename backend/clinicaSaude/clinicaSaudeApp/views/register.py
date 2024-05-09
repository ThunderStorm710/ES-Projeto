from django.contrib.auth.decorators import login_required
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
            {"invalid": "user already exists", "message": False},
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

