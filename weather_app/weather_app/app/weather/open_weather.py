from requests import request
from flask import current_app as app
from json import loads

class GetWeather:    
    @classmethod
    def get_city_weather(self, city:str):
        api_url = 'https://api.openweathermap.org/data/2.5/weather'
        """ Get a city weather given a city name """
        params = {
            'params': {"q": city, 'appid': app.config['OPEN_WEATHER_API_TOKEN'], 'units': 'metric'}
        }
        res = request('GET',url=api_url , **params)
        body = loads(res.text)
        
        return (res.status_code, body)