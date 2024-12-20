from rest_framework import viewsets # type: ignore
from .models import Hauberge, Resident, BlackList, Reservation, HaubergeResident
from .serializer import HaubergeSerializer, ResidentSerializer, BlackListSerializer, ReservationSerializer, HaubergeResidentSerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated
from .permission import IsAdminOrStaffForHauberge,IsStaffOrAdminPermission,IsAdminOrStaffOrAuthenticatedForResident,IsAdminOrStaffOrAuthenticatedForReservation,IsAdminOrStaffForBlackList


class HaubergeViewSet(viewsets.ModelViewSet):
    queryset = Hauberge.objects.all()
    serializer_class = HaubergeSerializer
    permission_classes = [IsAuthenticated, IsAdminOrStaffForHauberge]
class ResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer
    permission_classes = [IsAuthenticated, IsAdminOrStaffOrAuthenticatedForResident]
    
    
    
    

class BlackListViewSet(viewsets.ModelViewSet):
    queryset = BlackList.objects.all()
    serializer_class = BlackListSerializer
    permission_classes = [IsAuthenticated, IsAdminOrStaffForBlackList]
    

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated, IsAdminOrStaffOrAuthenticatedForReservation]
    

class HaubergeResidentViewSet(viewsets.ModelViewSet):
    queryset = HaubergeResident.objects.all()
    serializer_class = HaubergeResidentSerializer
    
