from django.test import TestCase
from unittest.mock import patch
from forecast.services.openweather_service import OpenWeatherService


class TestOpenWeatherService(TestCase):
    @patch('forecast.services.openweather_service.requests.get')
    def test_get_forecast(self, mock_get):
        # Mock the API response
        mock_get.return_value.json.return_value = {
            'daily': [{'dt': 1627776000, 'temp': {'min': 20, 'max': 30}}] * 7
        }
        mock_get.return_value.raise_for_status.return_value = None

        forecast = OpenWeatherService.get_forecast(25.6866, -100.3161)

        self.assertEqual(len(forecast), 7)
        self.assertEqual(forecast[0]['temp']['min'], 20)
        self.assertEqual(forecast[0]['temp']['max'], 30)

    @patch('forecast.services.openweather_service.requests.get')
    def test_get_forecast_api_error(self, mock_get):
        mock_get.side_effect = Exception("API Error")

        with self.assertRaises(Exception):
            OpenWeatherService.get_forecast(25.6866, -100.3161)
