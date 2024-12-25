from django.shortcuts import render
import urllib.request
import json
from django.conf import settings

def index(request):
    api_key = settings.OPENWEATHER_API_KEY
    if request.method == 'POST':
        city = request.POST['city']
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
        source = urllib.request.urlopen(url).read()
        list_of_data = json.loads(source)

        data = {
            "country_code" : list_of_data ['sys']['country'],
            "coordinate" : str(list_of_data['coord']['lon']) + ', ' + 
            str(list_of_data['coord']['lat']),
            "temp" : str(list_of_data['main']['temp'])+ ' °C',
            "pressure" : str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']), 
            "main" : str(list_of_data['weather'][0]['main']),
            "description": str(list_of_data['weather'][0]['description']),
            "icon" : list_of_data['weather'][0]['icon'],
        }
        print(data) # dislay on the terminal
    else:
        data = {}
    return render(request, 'weatherApp/index.html', {'data': data}) #use context