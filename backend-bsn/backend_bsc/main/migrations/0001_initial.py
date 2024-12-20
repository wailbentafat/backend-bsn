# Generated by Django 5.1.4 on 2024-12-19 23:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlackList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('numero_carte_identite', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hauberge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('maison', 'Maison'), ('camp', 'Camp')], max_length=10)),
                ('capacite', models.IntegerField()),
                ('nom', models.CharField(max_length=255)),
                ('emplacement', models.CharField(max_length=255)),
                ('adresse', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=20)),
                ('nbr_personne_reserve', models.IntegerField()),
                ('disponibilite', models.BooleanField()),
                ('image_list', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('date_naissance', models.DateField()),
                ('lieu_naissance', models.CharField(max_length=255)),
                ('sexe', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], max_length=10)),
                ('numero_carte_identite', models.CharField(max_length=50, unique=True)),
                ('permission_parentale', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_chambre', models.IntegerField()),
                ('date_entree', models.DateField()),
                ('date_sortie', models.DateField()),
                ('nature_reservation', models.CharField(choices=[('Gratuit', 'Gratuit'), ('Non Gratuit', 'Non Gratuit')], max_length=20)),
                ('restauration_montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hauberge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hauberge')),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.resident')),
            ],
        ),
        migrations.CreateModel(
            name='HaubergeResident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hauberge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hauberge')),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.resident')),
            ],
        ),
    ]
