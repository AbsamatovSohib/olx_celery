from django.db import models


class Home(models.Model):
    price = models.CharField(max_length=20, null=True, blank=True)
    content = models.CharField(max_length=127)

    valume = models.CharField(max_length=127, null=True, blank=True)
    address = models.CharField(max_length=127, null=True, blank=True)
