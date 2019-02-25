from demo.models import Patient
from demo.serializers import PatientSerializer
from rest_framework import filters, viewsets


class PatientViewset(viewsets.ModelViewSet):
  queryset = Patient.objects.all()
  serializer_class = PatientSerializer
  filter_backends = (filters.SearchFilter,)
  search_fields = ('firstname', 'lastname')
