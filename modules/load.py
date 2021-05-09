import pandas as pd

from airflow.providers.mysql.hooks.mysql import MySqlHook
from datetime import datetime

def load_review_data(data):
    mysql_hook = MySqlHook(mysql_conn_id='sky')
    engine = mysql_hook.get_sqlalchemy_engine()
    connection = engine.connect()
    pd.to_sql(
        name='review',
        con=connection,
        if_exists='append',
        index=False
    )
    connection.close()
    engine.dispose()

