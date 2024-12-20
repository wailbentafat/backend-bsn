from rest_framework import serializers # type: ignore
from .models import Hauberge, Resident, BlackList, Reservation, HaubergeResident


class HaubergeSerializer(serializers.ModelSerializer):
    image_list = serializers.JSONField(required=False)
    offres = serializers.JSONField(required=False)

    class Meta:
        model = Hauberge
        fields = ['id', 'type', 'capacite', 'nom', 'emplacement', 'adresse', 'email', 'password', 
                  'telephone', 'nbr_personne_reserve', 'disponibilite', 'image_list', 'offres']
        extra_kwargs = {'password': {'write_only': True}}

class ResidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = ['id', 'nom', 'prenom', 'date_naissance', 'lieu_naissance', 'sexe', 'numero_carte_identite', 
                  'permission_parentale']


class BlackListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlackList
        fields = ['id', 'nom', 'prenom', 'numero_carte_identite']


class ReservationSerializer(serializers.ModelSerializer):
    hauberge = HaubergeSerializer(read_only=True) 
    resident = ResidentSerializer(read_only=True) 

    class Meta:
        model = Reservation
        fields = ['id', 'hauberge', 'resident', 'numero_chambre', 'date_entree', 'date_sortie', 
                  'nature_reservation', 'restauration_montant']



class HaubergeResidentSerializer(serializers.ModelSerializer):
    hauberge = HaubergeSerializer(read_only=True)
    resident = ResidentSerializer(read_only=True)

    class Meta:
        model = HaubergeResident
        fields = ['id', 'hauberge', 'resident']
