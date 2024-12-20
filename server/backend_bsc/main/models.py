from datetime import date
from django.db import models
from django.core.exceptions import ValidationError



class Hauberge(models.Model):
    TYPE_CHOICES = [
        ('maison', 'Maison'),
        ('camp', 'Camp'),
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    capacite = models.IntegerField()
    nom = models.CharField(max_length=255)
    emplacement = models.CharField(max_length=255) 
    adresse = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    nbr_personne_reserve = models.IntegerField()
    disponibilite = models.BooleanField()
    image_list = models.JSONField()  

    def __str__(self):
        return self.nom
    def clean(self):
        if self.nbr_personne_reserve>=self.capacite:
            raise ValidationError("NUMBEr rah bzaf habibi")
    def save(self,*args,**kwargs):
        self.disponibilite=self.nbr_personne_reserve<self.capacite
        super().save(*args, **kwargs)    


class Resident(models.Model):
    SEXE_CHOICES = [
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
    ]
    
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=255)
    sexe = models.CharField(max_length=10, choices=SEXE_CHOICES)
    numero_carte_identite = models.CharField(max_length=50, unique=True)
    permission_parentale = models.BooleanField()

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    def clean(self):
        age = date.today().year - self.date_naissance.year
        if age < 18 and not self.permission_parentale:
            raise ValidationError("Parental permission is required for residents under 18.")

class BlackList(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    numero_carte_identite = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    

class Reservation(models.Model):
    NATURE_CHOICES = [
        ('Gratuit', 'Gratuit'),
        ('Non Gratuit', 'Non Gratuit'),
    ]
    
    hauberge = models.ForeignKey(Hauberge, on_delete=models.CASCADE)
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    numero_chambre = models.IntegerField()
    date_entree = models.DateField()
    date_sortie = models.DateField()
    nature_reservation = models.CharField(max_length=20, choices=NATURE_CHOICES)
    restauration_montant = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Reservation #{self.id} - {self.hauberge.nom}"
    def clean(self):
        if self.date_entree<=self.data_sortie:
            raise ValidationError("The departure date must be after the entry date.")
        if self.hauberge.nbr_personne_reserve+1>self.hauberge.capacite:
            raise ValidationError("The hauberge does not have enough capacity for this reservation")  
        overlapping_reservation=Reservation.objects.filter(
            Hauberge=self.hauberge,
            numero_chambre=self.numero_chambre,
            data_sortie=self.date_sortie,
            data_entrie=self.date_entree,
            
        ).exists()
        if overlapping_reservation:
            raise ValidationError("this room is already resreved  for the selected date")
        def save(self, *args, **kwargs):
            if not self.restauration_montant:
                days=(self.data_sortie-self.date_entree).days
                self.restauration_montant=100*days  #TODO
                super().save(*args, **kwargs)
                

class HaubergeResident(models.Model):
    hauberge = models.ForeignKey(Hauberge, on_delete=models.CASCADE)
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.resident.nom} in {self.hauberge.nom}"
    def clean(self):
        if HaubergeResident.objects.filter(hauberge=self.hauberge, resident=self.resident).exists():
            raise ValidationError("This resident is already linked to the hauberge.")
        