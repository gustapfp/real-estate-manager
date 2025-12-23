from django.db import models


# Create your models here.
class Location(models.Model):
    cep = models.CharField(max_length=8)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, default="Brazil")
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.street} - {self.city} - {self.state} -  {self.country}"

    def point(self):
        if self.latitude and self.longitude:
            return (self.longitude, self.latitude)
        return None
