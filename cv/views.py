from django.shortcuts import render
from rest_framework import viewsets
from .models import Cv
from .serializers import CvSerializer

# Create your views here.
class CvView(viewsets.ModelViewSet):
  queryset = Cv.objects.all()
  serializer_class = CvSerializer
