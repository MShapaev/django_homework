from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.CharField(max_length=6)
    slug = models.SlugField(max_length=255, unique=True, null=False)
