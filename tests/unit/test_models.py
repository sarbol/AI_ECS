import unittest
from app.models import User, EnvironmentData

class TestModels(unittest.TestCase):
    
    def test_create_user(self):
        user = User(name="Test User", email="test@example.com", preferences={})
        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.email, "test@example.com")

    def test_create_environment_data(self):
        env_data = EnvironmentData(temperature=22.5, humidity=45.0, air_quality=30.0)
        self.assertEqual(env_data.temperature, 22.5)
        self.assertEqual(env_data.humidity, 45.0)

if __name__ == '__main__':
    unittest.main()