from rest_framework import viewsets # type: ignore
from .models import Hauberge, Resident, BlackList, Reservation, HaubergeResident
from .serializer import HaubergeSerializer, ResidentSerializer, BlackListSerializer, ReservationSerializer, HaubergeResidentSerializer

class HaubergeViewSet(viewsets.ModelViewSet):
    queryset = Hauberge.objects.all()
    serializer_class = HaubergeSerializer

class ResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer
    
    
    
    

class BlackListViewSet(viewsets.ModelViewSet):
    queryset = BlackList.objects.all()
    serializer_class = BlackListSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class HaubergeResidentViewSet(viewsets.ModelViewSet):
    queryset = HaubergeResident.objects.all()
    serializer_class = HaubergeResidentSerializer
