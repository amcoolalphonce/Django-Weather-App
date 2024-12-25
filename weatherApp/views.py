from django.shortcuts import render
import urllib.request
import json

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=05f40e6e6f6c875717eb46a727da05dd').read()
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