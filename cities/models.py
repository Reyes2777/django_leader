from django.db import models


class Region(models.Model):
    """
    Model application regions:
        .. code-block:: python3

            code (int): id number unique
            name (str): name of region
    """
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class City(models.Model):
    """
    Model application city:
        .. code-block:: python3

            code (int): id number unique
            name (str): name of region
            is_active (bool): is value of region is active or not
            regions (list): list of region with relation many to many in regions
    """
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)
    is_active = models.BooleanField()
    regions = models.ManyToManyField(Region)

    def __str__(self):
        return self.name
