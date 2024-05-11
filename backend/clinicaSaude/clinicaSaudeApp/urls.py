from django.urls import path
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    #path('login', views.Login),
    path('register/', views.register_view),

    path('doctors/', views.create_doctor_view),
    #path('doctors/', views.get_doctors_view),
    path('doctor/<int:id>', views.get_doctor_by_id_view),

    path('appointments/', views.create_appointment_view),
    #path('appointments/', views.get_all_appointments_view),
    path('appointment/<int:id>', views.get_appointment_by_id_view),

    #path('payments/', views.create_payment_view),
    path('payments/', views.get_all_payments_view),
    path('payment/<int:id>', views.get_payment_by_id_view),

    path('specialty/', views.create_specialty_view),
    #path('specialty/', views.get_all_specialties_view),

    #path('logout', views.Logout),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),

]

