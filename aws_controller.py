''' Util functions to interface with Athena databases '''
import os
import pandas as pd
import psycopg2
import aws_config


def get_data():
    ''' Load all data into dataframe '''
    conn = psycopg2.connect(host=aws_config.rds_host, port=aws_config.rds_port,
                            dbname=aws_config.db_name, user=aws_config.db_username,
                            password=aws_config.db_password)

    df = pd.read_sql('SELECT * FROM "SensorData"', conn)
    json_df = pd.DataFrame(df['data'].values.tolist())
    df = pd.concat([df[['time', 'test', 'device_id']], json_df], axis=1)
    return df
