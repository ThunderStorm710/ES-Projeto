from django.urls import path

from backend.clinicaSaude.clinicaSaudeApp import views

urlpatterns = [
    path('login', views.Login),
    path('register', views.Register),
    path('logout', views.Logout),

]
