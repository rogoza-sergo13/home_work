import json
import requests
from pydantic import BaseModel, validator, Extra


class Temperature(BaseModel):
    class Config:
        extra = Extra.forbid

    temp: float
    feels_like: float
    temp_min: float
    temp_max: float

    @validator('temp')
    def transform(cls, value):
        return round(value * 9 / 5 + 32.2)


class Weather(BaseModel):
    temperature: Temperature
    pressure: int
    description: str
    name: str


class Location:

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_weather(self):
        r = requests.get(f'https://fcc-weather-api.glitch.me/api/current?lat={self.latitude}&lon={self.longitude}')
        try:
            if r.status_code != 200:
                raise Exception('Error request')
            j_l = json.loads(r.text)
            try:
                _feels_like_ = j_l.get['main']['feels_like']
            except:
                _feels_like_ = 0

            data = {
                'temperature': {
                    'temp': j_l['main']['temp'],
                    'feels_like': _feels_like_,
                    'temp_min': j_l['main']['temp_min'],
                    'temp_max': j_l['main']['temp_max']
                },
                'pressure': j_l['main']['pressure'],
                'description': j_l['weather'][0]['description'],
                'name': j_l['name']
            }
        except Exception:
            return None
        return Weather(**data)


location = Location(35, 139)
weather = location.get_weather()
print(f'In {weather.name} {weather.temperature.temp} F')
