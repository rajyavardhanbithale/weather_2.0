#!/usr/bin/python3

'''
 * No Modification should be Performed, Unless it is very Necessary.; otherwise, this code will go to shit.
 * A Python Program that uses The OpenWeather API to Perform Weather Forecasts.
 * Specifically Designed for Geeks for Geeks Hackathon: https://www.geeksforgeeks.org/.
 * Created by Rajyavardhan Bithale under Rage-Sec.
 * https://github.com/rajyavardhanbithale - rajyavardhanbithale@protonmail.com
'''

import requests
import time

class weather():

    def __init__(self,api,city,debug=False) -> None:
        self.key = api
        self.cityName = city

        self.debug = debug

        self.baseUrlWeather = "http://api.openweathermap.org/data/2.5/weather?"
        self.baseUrlForcast = "http://api.openweathermap.org/data/2.5/forecast?"

        self.baseUrlDayOne  = self.baseUrlWeather + "appid=" + self.key + "&q=" + self.cityName              # to be passed in weatherPresent
        self.baseUrlDayFour = self.baseUrlForcast + 'appid=' + self.key + '&q=' + self.cityName+ '&count=5'


    def weatherPresent(self):
        response = requests.get(self.baseUrlDayOne)
        jsonResponse = response.json()

        if self.debug:
            print(time.strftime('%A',time.localtime(jsonResponse['dt'])), # day
                time.strftime('%d %b %Y',time.localtime(jsonResponse['dt'])),   # date
                
                jsonResponse['name']+', '+jsonResponse['sys']['country'],       # region
                round(int(jsonResponse['main']['temp'])-273.15),                # temperature in C^o
                
                jsonResponse['weather'][0]['main'],                             # weather description
                jsonResponse['weather'][0]['id'],                               # icon ID
                self.iconCodeToName(jsonResponse['weather'][0]['id'],jsonResponse),   #icon name

                jsonResponse['weather'][0]['description'].title(),              # weather description in title
                jsonResponse['main']['humidity'],                               # humidity  (%)
                round(jsonResponse['wind']['speed']*3.6))                       # wind speed (km/h)           
            
        else:
            return (time.strftime('%A',time.localtime(jsonResponse['dt'])), # day
                time.strftime('%d %b %Y',time.localtime(jsonResponse['dt'])),   # date
                
                jsonResponse['name']+', '+jsonResponse['sys']['country'],       # region
                round(int(jsonResponse['main']['temp'])-273.15),                # temperature in C^o
                
                jsonResponse['weather'][0]['main'],                             # weather description
                jsonResponse['weather'][0]['id'],                               # icon ID
                self.iconCodeToName(jsonResponse['weather'][0]['id'],jsonResponse),   #icon name

                jsonResponse['weather'][0]['description'].title(),              # weather description in title
                jsonResponse['main']['humidity'],                               # humidity  (%)
                round(jsonResponse['wind']['speed']*3.6))                       # wind speed (km/h)  

    def forcastFuture(self):
        responseFocast = requests.get(self.baseUrlDayFour)
        jsonResponseForcast = responseFocast.json()
   
        temperature = [] 
        day = []
        icon = []
        iconCodeName = []

        for i in range(0,len(jsonResponseForcast['list'])):
            if i%8==0:
                r1 = round(jsonResponseForcast['list'][i]['main']['temp']-273.15)
                r2 = time.strftime('%A',time.localtime(jsonResponseForcast['list'][i]['dt']))
                r3 = jsonResponseForcast['list'][i]['weather'][0]['id']
            
                temperature.append(r1)
                day.append(r2)
                
                icon.append(r3)
                iconCodeName.append(self.iconCodeToName(r3,jsonResponseForcast))
            else:
                pass
                   
        if self.debug:
            print("",temperature,"\n",day,"\n",icon,"\n",iconCodeName)

        else:
            return temperature, day, icon,iconCodeName

    def iconCodeToName(self,id1,response):
        if 200<= id1 <=232:
            ico = 'cloud-lightning'
        elif 300<= id1 <=321:
            ico = 'cloud-drizzle'
        elif 500<= id1 <=531:
            ico = 'cloud-rain'
        elif 600<= id1  <=622:
            ico = 'cloud-snow'
        elif 700<= id1 <=781:
            ico = 'wind'
        elif 801<= id1 <=804:
            ico = 'cloud'
        elif 'n' in response['weather'][0]['icon']:
            ico = 'moon'
        else:
            ico = 'sun'
        return ico

# driver code
if __name__ == '__main__':

    app = weather('YOUR-API-KEY','raipur',debug=True)

    print("current weather".title())
    app.weatherPresent()

    print("\nweather forcast 5 days".title())

    app.forcastFuture()
