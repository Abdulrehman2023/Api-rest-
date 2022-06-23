from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import APi_default

class AddressSerial(ModelSerializer):
    class Meta:
        model = APi_default
        fields = '__all__'