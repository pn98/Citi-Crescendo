import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import City, Country, Continent

class UpdatePopulationView(APIView):
    def get(self, request):
        api_url = "https://world-population.p.rapidapi.com/population"
        headers = {"X-RapidAPI-Key": "your-api-key"}  # Replace with your API key

        response = requests.get(api_url, headers=headers)
        data = response.json()

        # Example: Assuming the API returns population data in the following format
        if data['ok']:
            world_population_data = data['body']

            # Update the population of continents, countries, and cities in the database
            for continent in world_population_data['continents']:
                cont, created = Continent.objects.get_or_create(name=continent['name'])
                cont.population = continent['population']
                cont.save()

            for country in world_population_data['countries']:
                cont = Continent.objects.get(name=country['continent'])
                ctry, created = Country.objects.get_or_create(name=country['name'], continent=cont)
                ctry.population = country['population']
                ctry.save()

            for city in world_population_data['cities']:
                ctry = Country.objects.get(name=city['country'])
                cty, created = City.objects.get_or_create(name=city['name'], country=ctry)
                cty.population = city['population']
                cty.save()

        return Response({"status": "Population data updated successfully!"})
