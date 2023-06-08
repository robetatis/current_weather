from dotenv import load_dotenv
import requests
import os
from city import city_name

def configure():
    load_dotenv()

def get_current_weather(api_key, city_name):
    url = "http://api.openweathermap.org/data/2.5/weather?appid=" + api_key + "&q=" + city_name
    response = requests.get(url).json()
    return response

def main():
    configure()
    API_KEY = os.getenv('API_KEY')    
    w = get_current_weather(api_key=API_KEY, city_name=city_name)
    for k, v in w.items():
        print(k, v)

if __name__ == '__main__':
    main()

