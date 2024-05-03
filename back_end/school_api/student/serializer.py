from dataclasses import fields
from pyexpat import model
from .models import Student2
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student2
        fields = '__all__'