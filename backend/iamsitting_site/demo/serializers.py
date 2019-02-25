from demo.models import Patient
from rest_framework import serializers


class PatientSerializer(serializers.ModelSerializer):
  class Meta:
    model = Patient
    fields = ('firstname', 'lastname', 'age', 'weight', 'height', 'creatinine', 'dose', 'frequency', 'id')
