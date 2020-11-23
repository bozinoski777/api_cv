from rest_framework import serializers
from .models import Cv

class CvSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cv
    fields = ('id', 'name', 'email', 'mobile', 'birthday', 'citizenship', 'github', 'linkedin')
