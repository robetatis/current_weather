from city import city_name
from dotenv import load_dotenv
import requests
import os

def configure():
    load_dotenv()

def get_current_weather(session, city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.getenv('api_key')}",
    r = session.get(url)
    return r.json()


def main():
    configure()
    s = requests.Session()
    w = get_current_weather(s, city_name)
    print(w)


if __name__ == '__main__':
    main()
