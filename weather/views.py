from django.shortcuts import render
import requests
from .models import City


def index(request):
    appid = 'fe3e5674f70396d36ac921ac22a50d5f'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        if res.get('cod') == 200:  # Проверка на успешный ответ
            city_inf = {
                'city': city.name,
                'temp': res["main"]["temp"],
                'icon': res["weather"][0]["icon"]
            }
        else:
            city_inf = {
                'city': city.name,
                'temp': 'N/A',  # или другое значение по умолчанию
                'icon': 'N/A'  # или другое значение по умолчанию
            }

        all_cities.append(city_inf)

    context = {'all_info': all_cities}
    return render(request, 'weather/index.html', context)
