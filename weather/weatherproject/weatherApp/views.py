from django.shortcuts import render
import requests

# Create your views here.
def home(request):
   
  

    return render(request,'home.html')

def weather(request):
    city=request.GET.get('city')
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=4523f1237a34b8f6086185c85c545a58'
    

    data=requests.get(url).json()
    print(data)
    payload={
        'city':data['name'],
        'weather':data['weather'][0]['main'],
        'icon':data['weather'][0]['icon'],
        'kelvin_temperature': int(data['main']['temp']),
        'celcius_temperature': int(data['main']['temp'] -273),
        'pressure':data['main']['pressure'],
        'humidity':data['main']['humidity'],
        'description' :data['weather'][0]['description']
    }
    context={'data':payload}
    return render(request,'weather.html',context)
