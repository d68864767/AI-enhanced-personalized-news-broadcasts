```python
import unittest
import json
from unittest.mock import patch, MagicMock
from news_scraper import NewsScraper

class TestNewsScraper(unittest.TestCase):
    def setUp(self):
        self.news_scraper = NewsScraper()

    @patch('news_scraper.requests.get')
    def test_get_news(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'status': 'ok',
            'articles': [{'title': 'Test News', 'description': 'Test Description'}]
        }
        mock_get.return_value = mock_response

        result = self.news_scraper.get_news()
        self.assertEqual(result, [{'title': 'Test News', 'description': 'Test Description'}])

    @patch('news_scraper.requests.get')
    def test_get_news_by_keyword(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'status': 'ok',
            'articles': [{'title': 'Test News', 'description': 'Test Description'}]
        }
        mock_get.return_value = mock_response

        result = self.news_scraper.get_news_by_keyword('Test')
        self.assertEqual(result, [{'title': 'Test News', 'description': 'Test Description'}])

    @patch('news_scraper.requests.get')
    def test_get_news_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'status': 'error',
            'message': 'Failed to fetch news'
        }
        mock_get.return_value = mock_response

        with self.assertRaises(Exception):
            self.news_scraper.get_news()

    @patch('news_scraper.requests.get')
    def test_get_news_by_keyword_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'status': 'error',
            'message': 'Failed to fetch news'
        }
        mock_get.return_value = mock_response

        with self.assertRaises(Exception):
            self.news_scraper.get_news_by_keyword('Test')

if __name__ == '__main__':
    unittest.main()
```
