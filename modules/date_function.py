import pandas as pd
from datetime import datetime, timedelta

def get_yesterday():
    today = datetime.today()
    today = pd.Timestamp(today).floor('d')
    yesterday = today - pd.Timedelta(days=1)
    return yesterday
