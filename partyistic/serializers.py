from rest_framework import serializers
from .models import Inspiration, Places, Planners, MusicBands ,PhotoSession, Fashion, Cars, Trip, Parties


class InspirationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspiration
        fields = "__all__"

# class ServicesSerializer(serializers.ModelSerializer):
#     cars = CarsSerializer()
#     places = PlacesSerializer()
#     class Meta:
#         model = Services
#         fields = '__all__'
#         fields = ('service_type', 'cars', 'places')  

class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = '__all__'

class PlannersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planners
        fields = '__all__'

class MusicBandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicBands
        fields = '__all__'

class PhotoSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoSession
        fields = '__all__'

class FashionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fashion
        fields = '__all__'

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


class PartiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parties
        fields = "__all__"