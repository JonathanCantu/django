# Generated by Django 5.1.5 on 2025-02-03 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atomic_number', models.IntegerField()),
                ('element', models.CharField(max_length=50)),
                ('symbol', models.CharField(max_length=4)),
                ('atomic_mass', models.FloatField(default=0.0)),
                ('number_of_neutrons', models.IntegerField(default=0)),
                ('number_of_protons', models.IntegerField(default=0)),
                ('number_of_electrons', models.IntegerField(default=0)),
                ('period', models.IntegerField(default=0)),
                ('group', models.IntegerField(default=0)),
                ('phase', models.CharField(default='none', max_length=10)),
                ('radioactive', models.BooleanField(default=False)),
                ('natural', models.BooleanField(default=True)),
                ('metal', models.BooleanField(default=True)),
                ('nonmetal', models.BooleanField(default=True)),
                ('metalloid', models.BooleanField(default=False)),
                ('type', models.CharField(default='none', max_length=20)),
                ('atomic_radius', models.FloatField(default=0.0)),
                ('electronegativity', models.FloatField(default=0.0)),
                ('first_ionization', models.FloatField(default=0.0)),
                ('density', models.FloatField(default=0.0)),
                ('melting_point', models.FloatField(default=0.0)),
                ('boiling_point', models.FloatField(default=0.0)),
                ('number_of_isotopes', models.IntegerField(default=0)),
                ('discoverer', models.CharField(default='none', max_length=50)),
                ('year', models.IntegerField(verbose_name=9999)),
                ('specific_heat', models.FloatField(default=0.0)),
                ('number_of_shells', models.IntegerField(default=0)),
                ('number_of_valence', models.IntegerField(default=0)),
            ],
        ),
    ]
