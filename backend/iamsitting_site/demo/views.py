from demo.models import Patient
from demo.utils import get_patient_dose
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


def get_calculations(request, pk):
  patient = get_object_or_404(Patient, pk=pk)
  if request.is_ajax() and request.method == "GET":
    calc = get_patient_dose(patient)
    return JsonResponse(calc)
