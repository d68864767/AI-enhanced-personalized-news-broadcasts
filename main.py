```python
import json
from news_scraper import NewsScraper
from user_profile import UserProfile
from ai_model import AIModel
from broadcast import Broadcast
from database import Database

def main():
    # Load configuration
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Initialize database
    db_config = config['database']
    db = Database(db_config['host'], db_config['port'], db_config['user'], db_config['password'], db_config['database'])

    # Initialize news scraper
    scraper_config = config['news_scraper']
    scraper = NewsScraper(scraper_config['api_key'], scraper_config['base_url'])

    # Initialize AI model
    model_config = config['ai_model']
    model = AIModel(model_config['model_path'], model_config['tokenizer_path'])

    # Initialize broadcast
    broadcast_config = config['broadcast']
    broadcast = Broadcast(broadcast_config['output_dir'])

    # Get user profiles from database
    user_profiles = db.get_user_profiles()

    for user_profile in user_profiles:
        # Scrape news
        news = scraper.scrape(user_profile.interests)

        # Predict user's interest in each news article
        predictions = model.predict(news)

        # Generate personalized news broadcast
        personalized_news = broadcast.generate(news, predictions)

        # Save broadcast to file
        broadcast.save(personalized_news, user_profile.id)

if __name__ == "__main__":
    main()
```
