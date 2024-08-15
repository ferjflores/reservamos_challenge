from django.test import TestCase
from unittest.mock import patch
from forecast.services.reservamos_service import ReservamosService


class TestReservamosService(TestCase):
    @patch('forecast.services.reservamos_service.requests.get')
    def test_get_cities(self, mock_get):
        # Mock the API response
        mock_get.return_value.json.return_value = [
            {"city_name": "Monterrey", "country": "Mexico", "result_type": "city"},
            {"city_name": "Montemorelos", "country": "Mexico", "result_type": "city"},
        ]
        mock_get.return_value.raise_for_status.return_value = None

        cities = ReservamosService.get_cities("Mon")

        self.assertEqual(len(cities), 2)
        self.assertEqual(cities[0]['city_name'], "Monterrey")
        self.assertEqual(cities[1]['city_name'], "Montemorelos")

    @patch('forecast.services.reservamos_service.requests.get')
    def test_get_cities_no_results(self, mock_get):
        mock_get.return_value.json.return_value = []
        mock_get.return_value.raise_for_status.return_value = None

        cities = ReservamosService.get_cities("NonexistentCity")

        self.assertEqual(len(cities), 0)
