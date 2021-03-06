#!/usr/bin/python
 
import psycopg2
from config import config
 

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE user_visits (
            auto_id SERIAL PRIMARY KEY,
            user_id VARCHAR(255) NOT NULL,
            domain_name VARCHAR(255) NOT NULL,
            page_url VARCHAR(255) NULL,
            visit_ts TIMESTAMP NOT NULL
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # The next two lines are for creating table one by one
        # for command in commands:
            # cur.execute(commands)
        # create table
        cur.execute(commands)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        print('Table created!')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
 
if __name__ == '__main__':
    create_tables()
