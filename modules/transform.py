import pandas as pd
from date_function import get_yesterday

def drop_columns(data):
    data_subset = data.drop(columns=['userImage', 'replyContent', 'repliedAt'])
    return data_subset


def rename_columns(data):
    new_column_names = [
        'review_id', 'user_name', 'content', 'rating', 'thumbs_up_count', 
        'created_for_version', 'created_on'
    ]
    new_columns = dict(zip(data.columns, new_column_names))
    renamed_data = data.rename(columns=new_columns)
    return renamed_data


def filter_reviews(data):
    # mask reviews that were not written yesterday
    yesterday = get_yesterday()
    created_on_date_floor = data['created_on'].apply(lambda ts: ts.floor('d'))
    filtered_data = data.loc[(created_on_date_floor == yesterday), :]
    filtered_data = filtered_data.reset_index(drop=True)
    return filtered_data
    

def transform_review_data(data):
    transformed_data = (
        data.pipe(drop_columns)
            .pipe(rename_columns)
            .pipe(filter_reviews)
    )
    return transformed_data
