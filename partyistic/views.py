from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Inspiration, Services, Parties
from .permissions import IsOwnerOrReadOnly
from .serializers import InspirationSerializer, ServicesSerializer, PartiesSerializer


class InspirationList(ListCreateAPIView):
    queryset = Inspiration.objects.all()
    serializer_class = InspirationSerializer


class InspirationDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Inspiration.objects.all()
    serializer_class = InspirationSerializer

class ServicesList(ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ServicesDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer

class PartiesList(ListCreateAPIView):
    queryset = Parties.objects.all()
    serializer_class = PartiesSerializer


class PartiesDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Parties.objects.all()
    serializer_class = PartiesSerializer