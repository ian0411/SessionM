#!/usr/bin/python
 
import psycopg2
import csv
from config import config
 

def iter_row(cursor, size=5):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row
 
def get_result():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        query = """
            SELECT user_id, domain_name, page_url, MIN(visit_ts) AS first_visit, MAX(visit_ts) AS last_visit,
            SUM(CASE WHEN visit_ts >= now()::date - 7 THEN 1 ELSE 0 END) last_7,
            SUM(CASE WHEN visit_ts >= now()::date - 30 THEN 1 ELSE 0 END) last_30
            FROM user_visits
            GROUP BY user_id, domain_name, page_url
            ORDER BY user_id, domain_name
        """
        cur.execute(query)
        i = 0
        with open('results.csv', 'w') as f:
            write = csv.writer(f, delimiter = ',')
            for row in iter_row(cur, 5):
                print(row)
                write.writerow(row)
                i += 1
        cur.close()
        print('There are total {} records.'.format(i))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    get_result()