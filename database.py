```python
import psycopg2
import json
from user_profile import UserProfile

class Database:
    def __init__(self):
        with open('config.json') as config_file:
            data = json.load(config_file)
            self.config = data["database"]

        self.conn = psycopg2.connect(
            host=self.config["host"],
            port=self.config["port"],
            user=self.config["user"],
            password=self.config["password"],
            database=self.config["database"]
        )

        self.cursor = self.conn.cursor()

    def get_user_profile(self, user_id):
        self.cursor.execute("SELECT * FROM user_profiles WHERE id = %s", (user_id,))
        result = self.cursor.fetchone()
        if result is not None:
            return UserProfile.from_dict({
                'id': result[0],
                'interests': result[1]
            })
        else:
            return None

    def save_user_profile(self, user_profile):
        self.cursor.execute(
            "INSERT INTO user_profiles (id, interests) VALUES (%s, %s) ON CONFLICT (id) DO UPDATE SET interests = %s",
            (user_profile.id, user_profile.interests, user_profile.interests)
        )
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
```
