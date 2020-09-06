import json
import pandas as pd
import sqlalchemy

from google_play_scraper import reviews
from google_play_scraper.features.reviews import ContinuationToken

def load_continuation_token():
    """Load and re-pack data into a google play scraper continuation token -
    adapted from https://stackoverflow.com/questions/12309269/
    
    Args:
        None
            
    Returns:
        continuation_token (ContinuationToken): 
            indicates the next reviews to scraped
    """
    
    with open('token_data.json', 'r', encoding='utf-8') as json_file:
        token_data = json.load(json_file)

    token_data = tuple(token_data)
    continuation_token = ContinuationToken(*token_data)
    return continuation_token

def get_data(num_reviews):
    """Get review data by loading the continuation token, fetching, preprocessing 
    and inserting the review data and saving the new continuation token
    
    Args:
        num_reviews (int): number of reviews to be fetched 
    
    Returns:
        None
    """
    
    try:
        continuation_token = load_continuation_token()
        
        data, _ = reviews(
            'com.tgc.sky.android', 
            lang='en',
            count=num_reviews, 
            continuation_token=continuation_token
        )
    except:
        data, continuation_token = reviews(
            'com.tgc.sky.android', 
            lang='en',
            count=num_reviews
        )
    
    return data, continuation_token

def preprocess(data): 
    """Load data into a dataframe and preprocess by dropping and renaming
    features
    
    Args: 
        data (list): 
            data from google play scraper's reviews function
            contains review data in the form of dictionaries
        
    Returns:
        preprocessed_data (dataframe):
    """
    
    column_names = [
        'userName', 'content', 'score', 
        'thumbsUpCount', 'reviewCreatedVersion', 'at'
    ]
    new_column_names = [
        'user_id', 'review', 'rating', 
        'thumbs_up_count', 'version', 'datetime_created'
    ]
    column_map = dict(zip(column_names, new_column_names))

    preprocessed_data = pd.DataFrame(data) 
    preprocessed_data = preprocessed_data[column_names] # subset columns
    preprocessed_data.rename(columns=column_map, inplace=True) # rename columns
    return preprocessed_data

def insert_review_data(data, connection):
    """Insert review data into local MySQL database
    
    Args:
        data (dataframe): contains preprocessed review data
        
    Returns:
        None
    """
    
    data.to_sql(
        'reviews', 
        con=connection, 
        if_exists='append', 
        index=False,
        method='multi'
    )

def save_continuation_token(continuation_token):
    """Unpack and save the google play scraper continuation token into a 
    JSON file - adapted from https://stackoverflow.com/questions/12309269/
    
    Args:
        continuation_token (ContinuationToken): 
            indicates the next reviews to scraped
            
            refer to https://github.com/JoMingyu/google-play-scraper or
            help(ContinuationToken) after importing ContinuationToken
            from google_play_scraper.features.reviews
            
    Returns:
        None
    """
    
    token_data = continuation_token.unpack()
    with open('token_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(token_data, json_file, ensure_ascii=False, indent=4)
