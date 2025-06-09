from django.db import models
# At least generation 1 Pokemons (first 151 Pokemons)
# Create your models here.

# https://pokeapi.co/api/v2/pokemon/1

class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Pokemon(models.Model):
    name = models.CharField(max_length=200)
    photo_url = models.URLField()

    type = models.ManyToManyField(Type, related_name="pokemon_set", verbose_name="Type")
    
    def __str__(self):
        return self.name


    


 