from rest_framework import viewsets, filters
from rest_api.serializers import LocalImageSerializer # import our serializer
from blog.models import LocalImage # import our model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from braces.views import CsrfExemptMixin
from django.views.decorators.csrf import csrf_protect, csrf_exempt

class LocalImageViewSet(viewsets.ModelViewSet, CsrfExemptMixin):
    queryset = LocalImage.objects.all()
    serializer_class = LocalImageSerializer
    authentication_classes = []

    @csrf_exempt
    def post(self, request, format=None):
       serializer = LocalImageSerializer(data=request.data, files=request.FILES)
       if serializer.is_valid():
           serializer.save()
           content = {'please move along': 'nothing to see here'}
           return Response(content, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


