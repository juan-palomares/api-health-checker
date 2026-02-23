"""
Unit Tests for API health checker.
"""

import unittest
from unittest.mock import patch, Mock
import requests
from api_health_check import check_api


class TestAPIHealthCheck(unittest.TestCase):

    def test_healthy_api(self):
        """Test that a healthy API returns True."""
        api_config = {
            "name": "Test API",
            "url": "https://example.com/api",
            "expected_status": 200
        }


        #Mock the requests.get call
        with patch('api_health_check.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.elapsed.total_seconds.return_value = 0.5
            mock_get.return_value = mock_response

            result = check_api(api_config)
            self.assertTrue(result)

    def test_unhealthy_api(self):
        """Test that an API with wrong status code reutrns False"""
        api_config = {
            "name": "Test API",
            "url": "https://example.com/api",
            "expected_status": 200
        }

        with patch ('api_health_check.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 500
            mock_response.elapsed.total_seconds.return_value = 0.5
            mock_get.return_value = mock_response

            result = check_api(api_config)
            self.assertFalse(result)

    def test_timeout(self):
        """Test that timeout exceptions are handled"""
        api_config = {
            "name": "Test API",
            "url": "https://example.com/api",
            "expected_status": 200
        }

        with patch ('api_health_check.requests.get') as mock_get:
            mock_get.side_effect = requests.exceptions.Timeout()

            result = check_api(api_config)
            self.assertFalse(result)

    def test_connection_error(self):
        """Test that connections errors are handled"""
        api_config = {
            "name": "Test API",
            "url": "https://example.com/api",
            "expected_status": 200
        }

        with patch ('api_health_check.requests.get') as mock_get:
            mock_get.side_effect = requests.exceptions.ConnectionError()

            result = check_api(api_config)
            self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
   