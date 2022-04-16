
import requests
from django.shortcuts import redirect, render
from .models import History
from .forms import BunnerForm

# Create your views here.

def ispositive(fimit):
    abresult = fimit / 3600
    
    if abresult >= 0:
        output = '+' + str(abresult)
    else:
        output = '-' + str(abresult)
        
    return output

def weatherinfo(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=ed9c152e85cf3ae7cb27634a19c044e7'
    cities = History.objects.all()
    err_msg = ''
    color_msg = ''
    #con ='http://api.countrylayer.com/v2/alpha/{}?access_key=9c6a0fb116641b93c90766f720c9c804' 
    #vreq = requests.get(con.format('Ng')).json()
    #hui = vreq['name']
    if request.method == "POST":
        form = BunnerForm(request.POST)
        
        if form.is_valid():
            new_city = form.cleaned_data['name']
            city_count = History.objects.filter(name=new_city).count()
            
            if city_count == 0:
                req = requests.get(url.format(new_city)).json()
                if req['cod'] == 200:
                    form.save()
                    err_msg = 'City found sucessfully!!'
                    color_msg = 'success'
                else:
                    err_msg = 'City doesnt exist in the world'
                    color_msg = 'danger'
            else:
                err_msg = 'City already exists!!'
                color_msg = 'warning'
    else:        
        form = BunnerForm()
    
    
    msgg = err_msg
    c_msg = color_msg
    
    new_data = []
    for city in cities:
        req = requests.get(url.format(city)).json()
        #fun = requests.get(con.format(req['sys']['country'])).json()
        fimit = req['timezone']
        city_weather = {
            'city':city.name,
            'id': city.id,
            'temp':req['main']['temp'],
            'description':req['weather'][0]['description'],
            'wind': req['wind']['speed'],
            'humidity':req['main']['humidity'],
            'country':req['sys']['country'],
            'timezone':ispositive(fimit),
            #'country_full': fun.get('name'),
            'pressure':req['main']['pressure'],
            'icon':req['weather'][0]['icon'],
            'cod':req['cod'],   
           
        }
        new_data.append(city_weather)
        print(city_weather['timezone'])
        #print(city_weather['country_full'])
    #print(req)
    #print(vreq)
    #print(hui)
    
    context={ 'new_data':new_data, 'form':form, 'cities':cities, 'msgg':msgg, 'c_msg':c_msg }
    return render(request, 'weather/index.html', context)

def deleteweather(request, pk):
    cities = History.objects.get(id=pk)
    cities.delete()
    return redirect('weatherinfo')
    
   

