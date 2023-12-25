```python
class UserProfile:
    def __init__(self, id, interests):
        self.id = id
        self.interests = interests

    @staticmethod
    def from_dict(data):
        return UserProfile(data['id'], data['interests'])

    def to_dict(self):
        return {
            'id': self.id,
            'interests': self.interests
        }
```
