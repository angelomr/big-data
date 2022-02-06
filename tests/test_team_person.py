import unittest
import requests

class TestService(unittest.TestCase):
    def test_service_online(self, ):
        response = requests.get('http://localhost:5000/service')
        self.assertEqual(response.status_code, 200)

if __name__ == '__name':
    unittest.main()