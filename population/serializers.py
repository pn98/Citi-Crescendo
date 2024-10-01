from rest_framework import serializers
from .models import City, Country, Continent

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'population', 'country']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'population', 'continent']

class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = ['id', 'name', 'population']
