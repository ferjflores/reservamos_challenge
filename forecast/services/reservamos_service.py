import requests
from django.conf import settings
from forecast.logger import logger


class ReservamosService:
    @staticmethod
    def get_cities(city_name):
        logger.info(f'Fetching cities for query: {city_name}')
        try:
            response = requests.get(settings.RESERVAMOS_API_URL,
                                    params={"q": city_name})
            response.raise_for_status()
            cities = [city for city in response.json() if city['result_type'] == 'city']
            logger.debug(f'Found {len(cities)} cities')
            return cities
        except requests.RequestException as e:
            logger.error(f'Error fetching cities from Reservamos API: {str(e)}')
            raise
