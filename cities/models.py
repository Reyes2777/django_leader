from django.db import models


class City(models.Model):
    """
    Model application city:
        .. code-block:: python3

            code (int): id number unique
            name (str): name of region
            is_active (bool): is value of region is active or not
    """
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name


class Region(models.Model):
    """
    Model application regions:
        .. code-block:: python3

            code (int): id number unique
            name (str): name of region
            cities (list): list of region with relation many to many in regions
    """
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)
    cities = models.ManyToManyField(City)

    def __str__(self):
        return self.name
