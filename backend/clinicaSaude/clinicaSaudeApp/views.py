from django.shortcuts import render

# Create your views here.
@api_view(["GET"])
@login_required
def get_drafts_view(request):
    user = request.user
    info = Quiz.objects.filter(
        Q(author__user__username=user, finished=False) | Q(author__user__username=user, rejected=True)).order_by(
        "creation_date")

    if not info.exists():
        return JsonResponse({"error": True, "message": "No drafts found"})

    quizzes = []
    for i in range(len(info)):
        quizzes.append([info[i].name, info[i].id, info[i].creation_date])

    return JsonResponse({"quizzes": quizzes, "error": False, "message": ""}, status=200)


def Login(request):
    return render(request, 'login.html')

def Register(request):
    return render(request, 'register.html')

def Logout(request):
    return render(request, 'logout.html')

def Home(request):
    return render(request, 'home.html')

