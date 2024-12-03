from django.db import models

class Sun(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.name
