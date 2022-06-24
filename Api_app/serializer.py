from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import APi_default

from django.contrib.auth.models import User

class AddressSerial(ModelSerializer):
    class Meta:
        model = APi_default
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self,validated_data):
        user = User.objects.create(username= validated_data["username"])
        user.set_password(validated_data['password'])
        user.save()
        return user