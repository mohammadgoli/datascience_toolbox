# load postgre table as pandas dataframe

import psycopg2 as pg
import pandas.io.sql as psql

# no need to use double quots or single quots for names below
# just replace variables 
connection = pg.connect("host=localhost dbname=dbname user=user password=password")

# create cursor 
cur = connection.cursor()

# show table names 
cur.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
for table in cur.fetchall():
    print(table)


# load specific table's data as pandas dataframe 
dataframe = psql.read_sql('SELECT * FROM tablename', connection)

# show dataframe's head 
dataframe.head(5)