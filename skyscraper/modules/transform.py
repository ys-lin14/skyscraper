import pandas as pd
from modules.date_function import get_yesterday

def drop_columns(data):
    data_subset = data.drop(columns=['userImage', 'replyContent', 'repliedAt'])
    return data_subset


def rename_columns(data):
    new_column_names = [
        'review_id', 'user_name', 'content', 'rating', 'thumbs_up_count', 
        'version', 'last_modified'
    ]
    new_columns = dict(zip(data.columns, new_column_names))
    renamed_data = data.rename(columns=new_columns)
    return renamed_data


def convert_timestamps_to_string(data):
    transformed_data = data.copy()
    transformed_data['last_modified'] = (
        transformed_data['last_modified'].apply(lambda ts: ts.strftime('%Y-%m-%d %H:%M:%S'))
    )
    return transformed_data


def filter_reviews(execution_date, data):
    # mask reviews that were not written yesterday
    yesterday = get_yesterday(execution_date)
    created_on_date_floor = data['last_modified'].apply(lambda ts: ts.floor('d'))
    filtered_data = data.loc[(created_on_date_floor == yesterday), :]
    filtered_data = filtered_data.reset_index(drop=True)
    return filtered_data
    

def transform_review_data(execution_date, data):
    transformed_data = (
        data.pipe(drop_columns)
            .pipe(rename_columns)
            .pipe((filter_reviews, 'data'), execution_date=execution_date)
            .pipe(convert_timestamps_to_string)
    )
    return transformed_data
