from django.db import models
from django.core.urlresolvers import reverse

class Identitas(models.Model):
    Nama 	= models.CharField(max_length=200)
    NIM 	= models.CharField(max_length=200)
    SKS 	= models.CharField(max_length=200)

    def __unicode__(self):
        return self.Nama

    def get_absolute_url(self):
        return reverse('crud_edit', kwargs={'pk': self.pk})

