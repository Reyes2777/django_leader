from django.db import models


class Region(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class City(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)
    is_active = models.BooleanField()
    regions = models.ManyToManyField(Region)

    def __str__(self):
        return self.name
