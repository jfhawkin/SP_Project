from django.db import models
      
class Factor(models.Model):
    fact1 = models.CharField(max_length=25)
    def __unicode__(self):
        return self.name