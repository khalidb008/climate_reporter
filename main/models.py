from django.db import models


# Create your models here.
class climate(models.Model):
    city = models.CharField(max_length=50)
    temperature = models.FloatField()
    flood = models.FloatField()
    wind_speed = models.FloatField(default=0)
    carbon_emission = models.FloatField(default=0)
    rainfall = models.FloatField(default=0)

    def __str__(self):
        return self.city