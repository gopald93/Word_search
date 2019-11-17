from django.db import models
class City(models.Model):
    city_name = models.CharField(max_length=200)
    city_code = models.IntegerField(default=0)
    def __str__(self):
        return self.place_name        