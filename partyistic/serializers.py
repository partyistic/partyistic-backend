from rest_framework import serializers
from .models import Inspiration, Services, Parties


class InspirationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspiration
        fields = "__all__"

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"

class PartiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parties
        fields = "__all__"