from django.db import models


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


class HaubergeResident(models.Model):
    hauberge = models.ForeignKey(Hauberge, on_delete=models.CASCADE)
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.resident.nom} in {self.hauberge.nom}"
