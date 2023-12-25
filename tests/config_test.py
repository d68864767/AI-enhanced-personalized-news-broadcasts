```python
import json
import unittest

class TestConfig(unittest.TestCase):

    def setUp(self):
        with open('config.json') as config_file:
            self.config = json.load(config_file)

    def test_database_config(self):
        self.assertIn('database', self.config)
        self.assertIn('host', self.config['database'])
        self.assertIn('port', self.config['database'])
        self.assertIn('user', self.config['database'])
        self.assertIn('password', self.config['database'])
        self.assertIn('database', self.config['database'])

    def test_news_scraper_config(self):
        self.assertIn('news_scraper', self.config)
        self.assertIn('api_key', self.config['news_scraper'])
        self.assertIn('base_url', self.config['news_scraper'])

    def test_ai_model_config(self):
        self.assertIn('ai_model', self.config)
        self.assertIn('model_path', self.config['ai_model'])
        self.assertIn('tokenizer_path', self.config['ai_model'])

    def test_broadcast_config(self):
        self.assertIn('broadcast', self.config)
        self.assertIn('output_dir', self.config['broadcast'])

if __name__ == '__main__':
    unittest.main()
```
