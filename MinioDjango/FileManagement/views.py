from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializers import *
# Create your views here.


class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializers