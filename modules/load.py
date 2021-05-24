import pandas as pd
from airflow.providers.mysql.hooks.mysql import MySqlHook
from datetime import datetime

def replace_into(connection, review_values):
    sql = 'REPLACE INTO review VALUES (%s, %s, %s, %s, %s, %s, %s);'
    connection.execute(sql, review_values)
    
    
def load_review_data(data):
    mysql_hook = MySqlHook(mysql_conn_id='sky')
    engine = mysql_hook.get_sqlalchemy_engine(
            engine_kwargs={'connect_args': {'charset': 'utf8mb4'}}
    )
    connection = engine.connect()
    
    for review_values in data.itertuples(index=False, name=None):
        replace_into(connection, review_values)
    
    connection.close()
    engine.dispose()

