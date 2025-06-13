from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_age(self, value):
        if value <= 0 or value > 120:
            raise serializers.ValidationError("Enter a valid age between 1 and 120.")
        return value

    def validate_gender(self, value):
        if value.lower() not in ['male', 'female', 'other']:
            raise serializers.ValidationError("Gender must be 'Male', 'Female', or 'Other'.")
        return value