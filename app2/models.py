from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Comparative(models.Model):
    ''' This model stores the x and y coordinates for the graph '''

    name = models.CharField(max_length=100)
    x_axis = models.FloatField()
    y_axis = models.FloatField()

    def __unicode__(self):
        return self.name