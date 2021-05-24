from modules.extract import extract_review_data
from modules.transform import transform_review_data
from modules.load import load_review_data

def scrape_review_data(execution_date):
    data = extract_review_data(execution_date)
    transformed_data = transform_review_data(execution_date, data)
    load_review_data(transformed_data)
