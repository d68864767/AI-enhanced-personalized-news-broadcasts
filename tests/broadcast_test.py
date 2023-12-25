```python
import unittest
import os
import json
from unittest.mock import MagicMock
from broadcast import Broadcast

class TestBroadcast(unittest.TestCase):

    def setUp(self):
        self.output_dir = 'test_dir/'
        self.broadcast = Broadcast(self.output_dir)

    def test_generate(self):
        news = ['news1', 'news2', 'news3']
        predictions = [0.6, 0.4, 0.8]
        personalized_news = self.broadcast.generate(news, predictions)
        self.assertEqual(personalized_news, ['news1', 'news3'])

    def test_save(self):
        personalized_news = ['news1', 'news3']
        user_id = '1'
        self.broadcast.save(personalized_news, user_id)
        file_path = os.path.join(self.output_dir, f'user_{user_id}_news.json')
        with open(file_path, 'r') as f:
            saved_news = json.load(f)
        self.assertEqual(saved_news, personalized_news)

    def tearDown(self):
        file_path = os.path.join(self.output_dir, 'user_1_news.json')
        if os.path.exists(file_path):
            os.remove(file_path)

if __name__ == '__main__':
    unittest.main()
```
