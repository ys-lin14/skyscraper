import pandas as pd
from datetime import datetime, timedelta

def get_yesterday(execution_date):
    today = datetime.strptime(execution_date, '%Y-%m-%d')
    today = pd.Timestamp(today)
    yesterday = today - pd.Timedelta(days=1)
    return yesterday
