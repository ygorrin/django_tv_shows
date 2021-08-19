# Create your models here.
from django.db import models

#class Network(models.Model):
#    name = models.CharField(max_length=20)

class Show(models.Model):
    title = models.CharField(max_length=65)
    network = models.CharField(max_length=65)
    release_date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    desc = models.TextField()

    def __str__(self):
        return f"Show: {self.title}, {self.network}, {self.release_date}, {self.desc}"

    def __repr__(self):
        return f"Show: {self.title}, {self.network}, {self.release_date}, {self.desc}"

