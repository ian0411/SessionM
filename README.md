# SessionM
***************************************************************************************
Python3 Installation
<<folder name>> = SessionM
<<project name>> = user_visits
<<file name>> here can be any file that ended with .py extension name
***************************************************************************************
1. Check Python version:
   python3 -version
2. Where is the executable:
   which python3
3. Update and upgrade the system with apt-get:
   sudo apt-get install software-properties-common
   sudo add-apt-repository ppa:deadsnakes/ppa
   sudo apt-get update
   sudo apt-get -y update
4. Install Python 3.6:
   sudo apt-get install python3.6
5. Install packages through apt:
   sudo apt-get install python3-pip python3-dev
6. Install other packages:
   sudo apt-get install build-essential libssl-dev libffi-dev
7. Install virtual environment:
   sudo apt-get install -y python3-venv
8. Create a new virtualenv (go to the folder that you want to use first):
   mkdir <<folder name>>
   cd <<folder name>>
   python3 -m venv <<project name>>
9. Start the virtualenv:
   source <<project name>>/bin/activate
10. Stop the virtualenv:
   deactivate
11. View the folder:
   ls <<project name>>
12. Open command-line text editor (nano) and create a new file
   nano <<file name>>.py
13. Run Python:
   python3 <<file name>>.py



***************************************************************************************
PostgreSQL Installation
<<user name>> = ian
<<database name>> = user_visits
<<table name>> = user_visits
***************************************************************************************
1. Install PostgreSQL:
   sudo apt-get install postgresql libpq-dev postgresql-client postgresql-client-common
2. Go to new postgres account (this will become postgres command line):
   sudo -i -u postgres
3. Create a new user name:
   createuser <<user name>> -P --interactive
4. Create a new database:
   createdb <<database name>>
5. Connect to the database:
   psql <<database name>>
6. Display table list in the database:
   \dt
7. Display table (like 'SELECT * FROM <<table name>> 'query statement):
   \dd
8. Exit postgres account:
   Ctrl + D



***************************************************************************************
psycopg2 Installation
***************************************************************************************
1. Update package:
   sudo apt-get build-dep python3-psycopg2
2. Install psycopg2 (probably do this under virtualenv):
   sudo pip3 install psycopg2



***************************************************************************************
File Explanations
***************************************************************************************
1. database.ini:
   This file stores the connection string
2. config.py:
   The method that connect to PostgreSQL
3. user_visits.csv
   This is the raw data
4. user_visits.py
   This is for testing if the database connection is working
5. create_tables.py
   This will create the "user_visits" table
6. csv_to_tables.py
   This will convert data from CSV to PostgreSQL
7. query_last7.py
   This query will return the frequency of clients' visits in last 7 days (a week)
8. query_last30.py
   This query will return the frequency of clients' visits in last 30 days (a month)
9. query_first_last.py
   This query will return the first and last visit per domain
10. query_all.py
   This query will return the first and last visit per domain, and also the frequency of clients' visits in last 7 days and 30 days
11. query_all.output.py
   This query will return the first and last visit per domain, the frequency of clients' visits in last 7 days and 30 days, and also output a results.csv file
12. results.csv
   This is the query results from query_all.output.py script file
13. drop_tables.py
   This will drop the "user_visits" table. Be aware that you can't recover.
