# Create your models here.
from django.db import models

#class Network(models.Model):
#    name = models.CharField(max_length=20)


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # agregue claves y valores al diccionario de errores para cada campo no válido
        if len(postData['title']) < 2:
            errors["Titulo"] = "Titulo debe tener al menos 2 caracteres"
        if len(postData['network']) < 3:
            errors["Network"] = "Network debe tener al menos 3 caracteres"
        if not postData['release_date']:
            errors["Estreno"] = "Debe ingresar una fecha de estreno"
        if len(postData['desc']) < 3:
            errors["Descripcion"] = "La descripcion debe tener al meno 3 caracteres"
        if Show.objects.filter(title=postData['title']).exists():
            errors['Existe'] ='El titulo ya existe, favor ingresar otro'
        print(errors)
        return errors

    def edit_validator(self, postData):
        errors = {}
        print(postData['ed_title'])
        # agregue claves y valores al diccionario de errores para cada campo no válido
        if len(postData['ed_title']) < 2:
            errors["ed_title"] = "El largo del titulo debe ser mayor a 2 caracteres"
        if len(postData['ed_network']) < 3:
            errors["ed_network"] = "El largo del network debe ser mayor a 3 caracteres"
        if len(postData['ed_desc']) < 3:
            errors["ed_desc"] = "El largo de la descripcion debe ser mayor a 3 caracteres"
        if Show.objects.filter(title=postData['ed_title']).exclude(title=postData['ed_title']).exists():
            errors['existe'] ='El titulo ya existe, favor ingresar otro'
        print(errors)
        return errors

class Show(models.Model):
    title = models.CharField(max_length=65)
    network = models.CharField(max_length=65)
    release_date = models.DateField() #Fecha de estreno
    updated_at = models.DateTimeField(auto_now=True)
    desc = models.TextField()
    objects = ShowManager() 

    def __str__(self):
        return f"Show: {self.title}, {self.network}, {self.release_date}, {self.desc}"

    def __repr__(self):
        return f"Show: {self.title}, {self.network}, {self.release_date}, {self.desc}"

