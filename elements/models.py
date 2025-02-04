from django.db import models

#    group = models.CharField(max_length=15)

class Elements(models.Model):
    atomic_number = models.IntegerField()
    element = models.CharField(max_length=50)
    symbol = models.CharField(max_length=4)
    atomic_mass = models.FloatField(default=0.0)
    number_of_neutrons = models.IntegerField(default=0)
    number_of_protons = models.IntegerField(default=0)
    number_of_electrons = models.IntegerField(default=0)
    period = models.IntegerField(default=0)
    group = models.IntegerField(default=0)
    phase = models.CharField(max_length=10, default='none')
    radioactive = models.BooleanField(default=False)
    natural =  models.BooleanField(default=True)
    metal = models.BooleanField(default=True)
    nonmetal = models.BooleanField(default=True)
    metalloid = models.BooleanField(default=False)
    type = models.CharField(max_length=20, default='none')
    atomic_radius = models.FloatField(default=0.0)
    electronegativity = models.FloatField(default=0.0)
    first_ionization = models.FloatField(default=0.0)
    density = models.FloatField(default=0.0)
    melting_point = models.FloatField(default=0.0)
    boiling_point = models.FloatField(default=0.0)
    number_of_isotopes = models.IntegerField(default=0)
    discoverer = models.CharField(max_length=50, default='none')
    year = models.IntegerField(9999)
    specific_heat = models.FloatField(default=0.0)
    number_of_shells = models.IntegerField(default=0)
    number_of_valence = models.IntegerField(default=0)

