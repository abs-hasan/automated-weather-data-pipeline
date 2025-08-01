import os
import requests
from urllib.parse import urljoin
from airflow.hooks.base import BaseHook
from airflow.exceptions import AirflowException
from requests.exceptions import RequestException
from dotenv import load_dotenv 

load_dotenv()

class WeatherAPIHook(BaseHook):
    def __init__(self, timeout=10, retries=2):
        super().__init__()
        self.timeout = timeout
        self.retries = retries
        self.api_key = self._get_api_key_from_env()
        self.base_url = "https://api.openweathermap.org/data/2.5/"


    def _get_api_key_from_env(self):
        api_key = os.getenv("OPENWEATHER_API_KEY")
        if not api_key:
            raise AirflowException("OPENWEATHER_API_KEY environment variable not found.")
        return api_key


    ### Fetches raw current weather data for a given city from the OpenWeather API
    def fetch_current_weather(self, city):
        url = urljoin(self.base_url, "weather")
        params = {"q": city, "appid": self.api_key, "units": "metric"}

        for _ in range(self.retries):
            try:
                return requests.get(url, params=params, timeout=self.timeout).json()
            except requests.RequestException:
                pass
        return None
