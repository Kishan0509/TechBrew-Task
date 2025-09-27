import csv
import psycopg2
import os
import pandas as pd 


DATABASE_URL = 'postgresql://neondb_owner:npg_wIQdr2WV1fuz@ep-autumn-fire-a8xb3rau-pooler.eastus2.azure.neon.tech/neondb?sslmode=require&channel_binding=require'

csvpath = 'BCCI_Test_Batting.csv' 
tablename = 'BCCI_Test_Batting' 

def csv_neon(csvpath, tablename, db_url):
    try:
        connection = psycopg2.connect(db_url)
        cur = connection.cursor()
        print("Connected")

        with open(csvpath, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)  
            
            columns = ', '.join(header)
            placeholders = ', '.join(['%s'] * len(header))
            insert_sql = f"INSERT INTO {tablename} ({columns}) VALUES ({placeholders})"

            for row in reader:
                cur.execute(insert_sql, row)

        connection.commit()
        print(f"Data from {csvpath} successfully pushed to {tablename}.")

    except Exception as e:
        print(f"Error pushing data: {e}")
        if connection:
            connection.rollback() 

csv_neon(csvpath, tablename,DATABASE_URL)


         