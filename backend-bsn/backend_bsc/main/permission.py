from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Hauberge, Resident, BlackList, Reservation, HaubergeResident
from .serializer import HaubergeSerializer, ResidentSerializer, BlackListSerializer, ReservationSerializer, HaubergeResidentSerializer



class IsAdminOrStaffForHauberge(BasePermission):
    """
    Custom permission for Hauberge:
    - Admins: Full access.
    - Staff: Can PUT, DELETE, and GET.
    - Others: No access.
    """
    def has_permission(self, request, view):
        # Admins have full access
        if request.user and request.user.is_superuser:
            return True
        if request.user and request.user.is_staff:
            return request.method in ['PUT', 'DELETE', 'GET']
        return False



class IsStaffOrAdminPermission(BasePermission):
   
    def has_permission(self, request, view):
        if request.user and request.user.is_superuser:
            return True  
        if request.method in SAFE_METHODS and request.user and request.user.is_staff:
            return True  
        return False 

class IsAdminOrStaffOrAuthenticatedForResident(BasePermission):
    """
    Custom permission for Resident:
    - Authenticated users can POST and PUT.
    - Admins and staff can GET all or individual records.
    """
    def has_permission(self, request, view):
        if request.method in ['POST', 'PUT']:
            
            return request.user and request.user.is_authenticated
        
        if request.method in SAFE_METHODS:
            return request.user and (request.user.is_superuser or request.user.is_staff)

        return False
class IsAdminOrStaffOrAuthenticatedForReservation(BasePermission):
    """
    Custom permission for Reservation:
    - Admins and staff can GET all reservations.
    - Authenticated users can POST to create a reservation.
    """
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user and request.user.is_authenticated
        
        if request.method == 'GET':
            return request.user and (request.user.is_superuser or request.user.is_staff)

        return False
   

class IsAdminOrStaffForBlackList(BasePermission):
  
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
    
            if request.user and (request.user.is_superuser or request.user.is_staff):
                return True

           
            if request.user and request.user.is_authenticated:
                if view.action == 'list' or view.action == 'retrieve':
                    return True
        return False

    def has_object_permission(self, request, view, obj):
     
        if request.method == 'GET':
            return obj.user == request.user
        return False
