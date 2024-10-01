from django.urls import path
from .views import CityList, CountryList, ContinentList
from .views import UpdatePopulationView

urlpatterns = [
    path('cities/', CityList.as_view(), name='city-list'),
    path('countries/', CountryList.as_view(), name='country-list'),
    path('continents/', ContinentList.as_view(), name='continent-list'),
    path('update-population/', UpdatePopulationView.as_view(), name='update-population'),
]


