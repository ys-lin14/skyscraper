from extract import extract_review_data
from transform import transform_review_data
from load import load_review_data

def scrape_review_data():
    data = extract_review_data()
    transformed_data = transform_review_data(data)
    load_review_data(transformed_data)
