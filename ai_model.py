```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class AIModel:
    def __init__(self, user_profile, news_scraper):
        self.user_profile = user_profile
        self.news_scraper = news_scraper
        self.vectorizer = TfidfVectorizer(stop_words='english')

    def get_personalized_news(self):
        user_interests = self.user_profile.interests
        all_news = []
        for interest in user_interests:
            news = self.news_scraper.get_news_by_keyword(interest)
            all_news.extend(news)

        if not all_news:
            return []

        news_contents = [news['content'] for news in all_news]
        tfidf_matrix = self.vectorizer.fit_transform(news_contents)
        user_interests_matrix = self.vectorizer.transform(user_interests)

        cosine_similarities = cosine_similarity(user_interests_matrix, tfidf_matrix)
        recommended_news_indices = np.argsort(-cosine_similarities[0])

        return [all_news[i] for i in recommended_news_indices]
```
