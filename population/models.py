from django.db import models

class Continent(models.Model):
    name = models.CharField(max_length=100)
    population = models.BigIntegerField()

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)
    population = models.BigIntegerField()
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    population = models.BigIntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
