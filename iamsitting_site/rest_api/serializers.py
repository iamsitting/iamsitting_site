from rest_framework import serializers

from blog.models import LocalImage


class LocalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalImage
        fields = ('pk', 'file', ) # only serialize the primary key and the image field
