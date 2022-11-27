from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CarInfo

class CarInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarInfo
        fields = ["car_number", "owner_name", "picture", "owner_dob", "car_model", "car_type", "color", "date_of_reg", "region_of_reg", "date_created", "date_updated"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
