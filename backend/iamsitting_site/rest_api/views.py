import logging

from braces.views import CsrfExemptMixin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_api.serializers import LocalImageSerializer  # import our serializer

debug = logging.getLogger('debugger')


class UploadLocalImage(CsrfExemptMixin, APIView):
  authentication_classes = []

  def post(self, request, format=None):
   # serializer = LocalImageSerializer(data=request.data, files=request.FILES)
   form_data = request.data['form-data']
   debug.debug(form_data)
   serializer = LocalImageSerializer(data=request.data['file'])
   if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
