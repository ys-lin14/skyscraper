import pandas as pd
import time
from modules.date_function import get_yesterday
from google_play_scraper import Sort, reviews

def get_extraction_is_complete(execution_date, data):
    # return whether the batch contains any reviews from before yesterday
    yesterday = get_yesterday(execution_date)
    extraction_is_complete = data['at'].apply(lambda ts: ts < yesterday).any()
    return extraction_is_complete


def get_continue_extracting_reviews(execution_date, data):
    continue_extracting_reviews = not(
        get_extraction_is_complete(execution_date, data)
    )
    return continue_extracting_reviews


def extract_next_batch(continuation_token, app_id):
    results, continuation_token = reviews(
        app_id,
        continuation_token=continuation_token
    )
    next_batch = pd.DataFrame(results)
    return next_batch, continuation_token


def extract_review_data(execution_date, app_id='com.tgc.sky.android'):
    results, continuation_token = reviews(
        app_id,
        sort=Sort.NEWEST,
        count=200
    ) 
    review_data = pd.DataFrame(results)
    
    continue_extracting_reviews = get_continue_extracting_reviews(
        execution_date,
        review_data
    )
    while(continue_extracting_reviews):
        next_batch, continuation_token = extract_next_batch(
            continuation_token, 
            app_id=app_id
        )
        continue_extracting_reviews = get_continue_extracting_reviews(
            execution_date, 
            next_batch
        ) 
        review_data = review_data.append(next_batch, ignore_index=True)
        time.sleep(1)
            
    return review_data
