# Generated by Django 5.0.1 on 2024-02-08 14:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfe', '0007_alter_seance_dateseance'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='Identifiant_professeur',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pfe.teacher'),
            preserve_default=False,
        ),
    ]
