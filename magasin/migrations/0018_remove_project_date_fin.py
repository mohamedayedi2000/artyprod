# Generated by Django 4.1.7 on 2023-05-01 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0017_remove_project_date_debut'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='date_fin',
        ),
    ]
