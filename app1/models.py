from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Catagory(MPTTModel):

    ''' This table stores the hierarchy for catagory i.e employed ,unemployed, etc  '''

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    name = models.CharField(max_length=200)
    level = models.IntegerField()
    description = models.TextField()

    class MPTTMeta:
        order_insertion_by = ['name']

    def __unicode__(self):
        return self.name



GENDER_CHOICES = (("male", "Male"),("female", "Female"),("other", "Other"))

class Member(models.Model):

    ''' This models stores information about member  and to which '''

    name = models.CharField(max_length=200)
    catagory = models.ForeignKey(Catagory)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=50)
    description = models.TextField()

    def __unicode__(self):
        return self.name
