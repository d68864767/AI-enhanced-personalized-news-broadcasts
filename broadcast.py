```python
import os
import json

class Broadcast:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def generate(self, news, predictions):
        personalized_news = [news[i] for i, pred in enumerate(predictions) if pred > 0.5]
        return personalized_news

    def save(self, personalized_news, user_id):
        file_path = os.path.join(self.output_dir, f'user_{user_id}_news.json')
        with open(file_path, 'w') as f:
            json.dump(personalized_news, f, indent=4)
```
