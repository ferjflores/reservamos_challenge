from rest_framework.views import APIView
from rest_framework.response import Response
from forecast.services.reservamos_service import ReservamosService
from forecast.services.openweather_service import OpenWeatherService
from forecast.serializers import ForecastSerializer
from forecast.logger import logger


class ForecastView(APIView):
    def get(self, request):
        city_name = request.query_params.get('city')
        if not city_name:
            logger.warning('City parameter is missing')
            return Response({"error": "City parameter is required"}, status=400)

        logger.info(f'Fetching forecast for city: {city_name}')

        try:
            cities = ReservamosService.get_cities(city_name)
            logger.debug(f'Found {len(cities)} cities matching "{city_name}"')

            forecasts = []
            for city in cities:
                logger.debug(
                    f'Fetching forecast for {city["city_name"]}, {city["country"]}')
                forecast = OpenWeatherService.get_forecast(city['lat'], city['long'])
                formatted_forecast = [
                    {
                        "date": day['dt'],
                        "max_temp": day['temp']['max'],
                        "min_temp": day['temp']['min']
                    } for day in forecast
                ]
                forecasts.append({
                    "city": city['city_name'],
                    "country": city['country'],
                    "forecast": formatted_forecast
                })

            serializer = ForecastSerializer(forecasts, many=True)
            logger.info(f'Successfully fetched forecasts for {len(forecasts)} cities')
            return Response(serializer.data)

        except Exception as e:
            logger.error(f'An error occurred while fetching forecasts: {str(e)}')
            return Response({"error": "An unexpected error occurred"}, status=500)
