# Generated by Django 5.0.3 on 2024-03-16 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videogames', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogames',
            name='company',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Compañia'),
        ),
        migrations.AlterField(
            model_name='videogames',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='videogames',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre'),
        ),
    ]
