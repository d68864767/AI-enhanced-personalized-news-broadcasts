```python
import unittest
import json
from database import Database
from user_profile import UserProfile

class TestDatabase(unittest.TestCase):
    def setUp(self):
        with open('config.json') as config_file:
            data = json.load(config_file)
            self.config = data["database"]

        self.db = Database()
        self.test_user = UserProfile(1, ['tech', 'business'])

    def test_get_user_profile(self):
        # Save a test user profile
        self.db.save_user_profile(self.test_user)

        # Retrieve the user profile
        user_profile = self.db.get_user_profile(1)

        # Check if the retrieved user profile matches the saved one
        self.assertEqual(user_profile.id, self.test_user.id)
        self.assertEqual(user_profile.interests, self.test_user.interests)

    def test_save_user_profile(self):
        # Save a test user profile
        self.db.save_user_profile(self.test_user)

        # Retrieve the user profile
        user_profile = self.db.get_user_profile(1)

        # Check if the retrieved user profile matches the saved one
        self.assertEqual(user_profile.id, self.test_user.id)
        self.assertEqual(user_profile.interests, self.test_user.interests)

        # Update the user profile
        self.test_user.interests.append('sports')
        self.db.save_user_profile(self.test_user)

        # Retrieve the updated user profile
        updated_user_profile = self.db.get_user_profile(1)

        # Check if the retrieved user profile matches the updated one
        self.assertEqual(updated_user_profile.id, self.test_user.id)
        self.assertEqual(updated_user_profile.interests, self.test_user.interests)

    def tearDown(self):
        # Delete the test user profile
        self.db.cursor.execute("DELETE FROM user_profiles WHERE id = %s", (self.test_user.id,))
        self.db.conn.commit()
        self.db.close()

if __name__ == '__main__':
    unittest.main()
```
