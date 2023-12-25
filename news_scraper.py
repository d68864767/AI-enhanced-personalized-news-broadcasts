```python
import requests
import json

class NewsScraper:
    def __init__(self):
        with open('config.json') as config_file:
            self.config = json.load(config_file)
        self.api_key = self.config['news_scraper']['api_key']
        self.base_url = self.config['news_scraper']['base_url']

    def get_news(self, category='general', language='en', country='us'):
        url = f"{self.base_url}top-headlines?category={category}&language={language}&country={country}&apiKey={self.api_key}"
        response = requests.get(url)
        data = response.json()
        if data['status'] != 'ok':
            raise Exception('Failed to fetch news')
        return data['articles']

    def get_news_by_keyword(self, keyword, language='en', sortBy='relevancy'):
        url = f"{self.base_url}everything?q={keyword}&language={language}&sortBy={sortBy}&apiKey={self.api_key}"
        response = requests.get(url)
        data = response.json()
        if data['status'] != 'ok':
            raise Exception('Failed to fetch news')
        return data['articles']
```
