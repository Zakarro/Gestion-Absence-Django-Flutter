# Generated by Django 5.0.1 on 2024-02-11 15:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfe', '0008_attendance_identifiant_professeur'),
    ]

    operations = [
        migrations.AddField(
            model_name='filiere',
            name='Identifiant_Annee',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pfe.annee'),
            preserve_default=False,
        ),
    ]
