# Lambda function used to write inbound IoT sensor data to RDS MySQL database

import sys
import os
import json
import logging
import psycopg2

import rds_config

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#rds settings
rds_host  = rds_config.rds_host
rds_port = rds_config.rds_port
username = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

fields_for_json = ['temperature', 'pressure', 'humidity','oxidised',
                   'reduced', 'nh3', 'lux', 'pm1', 'pm25', 'pm10']


def lambda_handler(event, context):
    ''' Lambda handler '''
    processBatch(event)
    return {
        'statusCode' : 200
    }

def processBatch(event):
    ''' Connect to postgres and loop through batch submitted by Lambda
        No exception handling is used on the connection attempt because we want failed
        connection attempts to fail the function so that messages go back into the queue

    '''
    conn = psycopg2.connect(host=rds_host, port=rds_port, dbname=db_name, 
                            user=username, password=password)
    conn.autocommit = True

    cur = conn.cursor()

    try:
        json_col = json.dumps(event['data'])

        cur.execute('insert into "SensorData" ("time", "device_id", "test", "data")'
                    ' values (%s, %s, %s, %s)',
                    (event['time'], event['device_id'], True,
                    json_col))
    except psycopg2.IntegrityError:
        '''Duplicate primary key errors occur if Lambda calls this function more than once with the same message
        Preventing duplicate inserts and ignoring failed attempts allows this function to be idempotent '''
        logger.info('Integrity error: DeviceID=' + event['device_id'] +
                    ', DateTime=' + event['time'])
    except:
        logging.info('Error adding record')
        cur.close()
        conn.close()
        raise
        
    cur.close()
    conn.close()


    

