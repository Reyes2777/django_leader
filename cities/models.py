from django.db import models


class Region(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.code

    class Meta:
        ordering = ('code',)


class City(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)
    is_active = models.BooleanField()
    regions = models.ManyToManyField(Region)

    def __unicode__(self):
        return self.code

    class Meta:
        ordering = ('code',)
