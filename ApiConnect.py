import time
import random
import requests

cities = ['Blagoevgrad','Burgas','Dobrich','Gabrovo','Haskovo','Kardzhali','Kyustendil'
,'Lovech','Montana','Pazardzhik','Pernik','Pleven','Plovdiv','Razgrad','Ruse','Shumen','Silistra',
'Sliven','Smolyan','Sofia','Stara Zagora','Targovishte','Varna','Veliko Tarnovo','Vidin','Vratsa'
,'Yambol']
counter = 5
temperature =[0,0,0,0,0]
town =['','','','','']
index =0

#Displays current weather information for a 5 random cities
while counter>0:
    #print (counter)
    picker = random.randint(0,26)
    town[index] = cities[picker]
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+str(cities[picker])+'&appid=90903af72782a2121a72698325cf26fc')
    jsonRead=r.json() 
    temperature[index] = float(jsonRead['main']['temp'])
    index+=1        
    print ('The weather in ' +str(cities[picker])+ ' is ' + str(jsonRead['weather'][0]['main']))
    print ('The temperature in '+str(cities[picker])+ ' is ' + str(jsonRead['main']['temp']))
    print ('The humidity in '+str(cities[picker])+ ' is ' + str(jsonRead['main']['humidity']))
    #print (r.text)
    time.sleep(10)
    counter-=1
#Calculates de coldest and mean temperatures for the 5 cities above    
index = 4
coldest = temperature[index]
while index>=0:
    if temperature[index]<coldest:
        coldest = temperature[index]
        townIndex = index
    index-=1
meanTemperature = (temperature[0]+temperature[1]+temperature[2]+temperature[3]+temperature[4])/5
print ('The coldest temperature is: ' + str(coldest)+ ' recorded in '+str(town[townIndex]))
print ('The mean temperature is: ' + str(meanTemperature))

#Displays current weather information for a city of user's choosing
city = input('Please specify a city: ')
r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+str(city)+'&appid=90903af72782a2121a72698325cf26fc')
jsonRead=r.json()
print ('The weather in ' + city + ' is ' + str(jsonRead['weather'][0]['main']))
print ('The temperature in '+ city + ' is ' + str(jsonRead['main']['temp']))
print ('The humidity in '+ city + ' is ' + str(jsonRead['main']['humidity']))




