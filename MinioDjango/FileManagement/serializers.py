from rest_framework import serializers
from .models import *


class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"