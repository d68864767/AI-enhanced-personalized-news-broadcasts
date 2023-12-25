```python
import unittest
from user_profile import UserProfile

class TestUserProfile(unittest.TestCase):

    def setUp(self):
        self.user_profile = UserProfile('1', ['AI', 'Programming'])

    def test_init(self):
        self.assertEqual(self.user_profile.id, '1')
        self.assertEqual(self.user_profile.interests, ['AI', 'Programming'])

    def test_from_dict(self):
        data = {'id': '2', 'interests': ['Data Science', 'Machine Learning']}
        user_profile = UserProfile.from_dict(data)
        self.assertEqual(user_profile.id, '2')
        self.assertEqual(user_profile.interests, ['Data Science', 'Machine Learning'])

    def test_to_dict(self):
        user_profile_dict = self.user_profile.to_dict()
        self.assertEqual(user_profile_dict, {'id': '1', 'interests': ['AI', 'Programming']})

if __name__ == '__main__':
    unittest.main()
```
