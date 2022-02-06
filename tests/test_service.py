import unittest
import requests

class TestTeamPerson(unittest.TestCase):
    def test_team_person_online(self, ):
        response = requests.get('http://localhost:5000/post')
        self.assertEqual(response.status_code, 200)

if __name__ == '__name':
    unittest.main()