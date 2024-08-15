from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch


class TestForecastAPI(TestCase):
    @patch('forecast.services.reservamos_service.ReservamosService.get_cities')
    @patch('forecast.services.openweather_service.OpenWeatherService.get_forecast')
    def test_forecast_api(self, mock_get_forecast, mock_get_cities):
        # Mock the services
        mock_get_cities.return_value = [
            {"city_name": "Monterrey", "country": "Mexico", "lat": 25.6866,
             "long": -100.3161}
        ]
        mock_get_forecast.return_value = [
            {'dt': 1627776000, 'temp': {'min': 20, 'max': 30}} for _ in range(7)
        ]

        # Make a request to the API
        url = reverse('forecast') + '?city=Monterrey'
        response = self.client.get(url)

        # Check the response
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['city'], 'Monterrey')
        self.assertEqual(len(data[0]['forecast']), 7)

    def test_forecast_api_no_city(self):
        url = reverse('forecast')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "City parameter is required"})
