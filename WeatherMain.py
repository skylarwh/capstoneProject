'''
PROJECT: Get the current weather for a given zip, Optional: get users automatically
AUTHOR: Skylar Hillebrant
API: https://openweathermap.org/api
'''
#import libraries
import geocoder
import geopy
import requests



#Get users current Lat/long
g = geocoder.ip('me')
geolocator = geopy.Nominatim(user_agent='me')

lat = g.latlng[0]
lon = g.latlng[1]
print('Your Location has been found! Lattitude:{} Longitude:{}'.format(lat,lon))

#request open weather maps API data
owm_url = 'https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={}&lon={}&appid={}'
api_key = 'b5d704b686210275f8982fad7825de63'

print('CONNECTING TO OPEN WEATHER MAP........')
response = requests.get(owm_url.format(lat,lon,api_key))

if response.status_code == 200:
    print("CONNECTION ESTABLISHED")
else:
    print("CONNECTION FAILED")



#Get the weather forecast for users location



#Output




