import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=19eb6745f320141260eae2691d70959d'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    Cities = City.objects.all()

    weather_data = []

    for city in Cities:

        r = requests.get(url.format(city)).json()
        
        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    print(weather_data)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weatherapp/weather.html', context)