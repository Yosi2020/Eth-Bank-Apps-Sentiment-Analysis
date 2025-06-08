from google_play_scraper import reviews
import pandas as pd

def scrape_reviews(banks, reviews_per_bank=400):
    reviews_list = []
    for bank_name, app_id in banks.items():
        print(f"Scraping {reviews_per_bank} reviews for {bank_name}...")
        result, _ = reviews(app_id, lang='en', country='et', count=reviews_per_bank)
        for r in result:
            reviews_list.append({
                'review': r['content'],
                'rating': r['score'],
                'date': r['at'].strftime('%Y-%m-%d'),
                'bank': bank_name,
                'source': 'Google Play'
            })
    return pd.DataFrame(reviews_list)
