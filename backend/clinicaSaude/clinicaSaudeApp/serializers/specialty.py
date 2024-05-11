from rest_framework import serializers
from clinicaSaudeApp.models import Specialty


class GetSpecialty(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ["indicator"]






