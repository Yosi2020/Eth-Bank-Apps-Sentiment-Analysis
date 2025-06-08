import pandas as pd

def preprocess_reviews(df):
    # Remove duplicates
    df = df.drop_duplicates(subset='review').dropna(subset=['review'])
    
    # Normalize dates
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    
    return df
