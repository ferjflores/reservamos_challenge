import requests
from django.conf import settings
from forecast.logger import logger


class OpenWeatherService:
    @staticmethod
    def get_forecast(lat, lon):
        logger.info(f'Fetching forecast for coordinates: {lat}, {lon}')
        params = {
            "lat": lat,
            "lon": lon,
            "exclude": "current,minutely,hourly,alerts",
            "units": "metric",
            "appid": settings.OPENWEATHER_API_KEY
        }
        try:
            response = requests.get(settings.OPENWEATHER_API_URL, params=params)
            response.raise_for_status()
            forecast = response.json()['daily'][:7]
            logger.debug(f'Retrieved {len(forecast)} days of forecast data')
            return forecast
        except requests.RequestException as e:
            logger.error(f'Error fetching forecast from OpenWeather API: {str(e)}')
            raise
