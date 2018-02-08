#!/usr/bin/python
 
import psycopg2
from config import config
 
 
def csv_to_tables():
    """ copy table from csv file to the PostgreSQL database"""
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # read from csv file
        with open('user_visits.csv', 'r') as f:
            # skip the header row
            next(f)
            cur.copy_from(f, 'user_visits', sep=',')
        # commit the changes
        conn.commit()
        print('Data conversion from csv is completed!')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
 
if __name__ == '__main__':
    csv_to_tables()
