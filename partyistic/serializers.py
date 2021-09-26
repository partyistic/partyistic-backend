from rest_framework import serializers
from .models import Inspiration, Services, Parties, Cars, Places


class InspirationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspiration
        fields = "__all__"

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'

class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    # cars = CarsSerializer(serializers.ModelSerializer)
    # places = PlacesSerializer(serializers.ModelSerializer)
    class Meta:
        model = Services
        fields = '__all__'
        # fields = ('service_type', 'cars', 'places')  




class PartiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parties
        fields = "__all__"