```python
import unittest
from unittest.mock import Mock
from ai_model import AIModel

class TestAIModel(unittest.TestCase):

    def setUp(self):
        self.user_profile = Mock()
        self.news_scraper = Mock()
        self.ai_model = AIModel(self.user_profile, self.news_scraper)

    def test_get_personalized_news(self):
        self.user_profile.interests = ['technology', 'science']
        self.news_scraper.get_news_by_keyword.return_value = [
            {'content': 'This is a news about technology'},
            {'content': 'This is a news about science'},
            {'content': 'This is a news about sports'}
        ]

        personalized_news = self.ai_model.get_personalized_news()

        self.assertEqual(len(personalized_news), 2)
        self.assertIn('technology', personalized_news[0]['content'])
        self.assertIn('science', personalized_news[1]['content'])

    def test_get_personalized_news_no_interests(self):
        self.user_profile.interests = []
        self.news_scraper.get_news_by_keyword.return_value = []

        personalized_news = self.ai_model.get_personalized_news()

        self.assertEqual(personalized_news, [])

    def test_get_personalized_news_no_news(self):
        self.user_profile.interests = ['technology', 'science']
        self.news_scraper.get_news_by_keyword.return_value = []

        personalized_news = self.ai_model.get_personalized_news()

        self.assertEqual(personalized_news, [])

if __name__ == '__main__':
    unittest.main()
```
