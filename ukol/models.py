from django.db import models


class Entrepreneur(models.Model):

    name = models.CharField('Jméno', max_length=255)
    mail = models.CharField('E-mail', max_length=255, blank=True)
    ico = models.CharField('Ičo', max_length=8)
    objects = models.Manager()

    def __str__(self):
        return self.name
