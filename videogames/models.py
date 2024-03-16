from django.db import models

# Create your models here.
class VideoGames(models.Model):
    title = models.CharField(max_length=50, blank= True, null =True, verbose_name="Nombre")
    company = models.CharField(max_length = 50, blank=True,null =True, verbose_name ="Compañia")
    release_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'videogames'