from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_specialty(self, value):
        if not value.strip():
            raise serializers.ValidationError("Specialty cannot be empty.")
        return value

    def validate_contact(self, value):
        if not value.strip():
            raise serializers.ValidationError("Contact cannot be empty.")
        if len(value) < 10:
            raise serializers.ValidationError("Contact number is too short.")
        return value