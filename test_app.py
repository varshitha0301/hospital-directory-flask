import unittest
from app import app

class HospitalAppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_homepage_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hospital Directory', response.data)

    def test_invalid_route_returns_404(self):
        response = self.client.get('/hospital/999999')  # assuming this ID doesn't exist
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
