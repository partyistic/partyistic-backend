from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from .models import Inspiration, Places, Planners, MusicBands ,PhotoSession, Fashion, Cars, Trip, Parties
from .permissions import IsOwnerOrReadOnly
from .serializers import InspirationSerializer, PartiesSerializer, PlacesSerializer,PlannersSerializer,MusicBandsSerializer,PhotoSessionSerializer, FashionSerializer, CarsSerializer, TripSerializer


class InspirationList(ListCreateAPIView):
    queryset = Inspiration.objects.all()
    serializer_class = InspirationSerializer
class InspirationDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Inspiration.objects.all()
    serializer_class = InspirationSerializer


# class ServicesList(ListCreateAPIView):
    # queryset = Services.objects.all()
    # serializer_class = ServicesSerializer

# class ServicesDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    # queryset = Services.objects.all()
    # serializer_class = ServicesSerializer


class PlacesList(ListCreateAPIView):
    queryset = Places.objects.all()
    serializer_class = PlacesSerializer
class PlacesDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Places.objects.all()
    serializer_class = PlacesSerializer


class PlannersList(ListCreateAPIView):
    queryset = Planners.objects.all()
    serializer_class = PlannersSerializer
class PlannersDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Planners.objects.all()
    serializer_class = PlannersSerializer


class MusicBandsList(ListCreateAPIView):
    queryset = MusicBands.objects.all()
    serializer_class = MusicBandsSerializer
class MusicBandsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = MusicBands.objects.all()
    serializer_class = MusicBandsSerializer


class PhotoSessionsList(ListCreateAPIView):
    queryset = PhotoSession.objects.all()
    serializer_class = PhotoSessionSerializer
class PhotoSessionsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = PhotoSession.objects.all()
    serializer_class = PhotoSessionSerializer


class FashionList(ListCreateAPIView):
    queryset = Fashion.objects.all()
    serializer_class = FashionSerializer
class FashionDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Fashion.objects.all()
    serializer_class = FashionSerializer


class CarsList(ListCreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
class CarsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer

class TripsList(ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
class TripsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class PartiesList(ListCreateAPIView):
    queryset = Parties.objects.all()
    serializer_class = PartiesSerializer
class PartiesDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Parties.objects.all()
    serializer_class = PartiesSerializer