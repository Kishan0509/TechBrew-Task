import csv
import psycopg2
import os
import pandas as pd 

DATABASE_URL = 'postgresql://neondb_owner:npg_wIQdr2WV1fuz@ep-autumn-fire-a8xb3rau-pooler.eastus2.azure.neon.tech/neondb?sslmode=require&channel_binding=require'
csvpath = 'BCCI_Odi_Batting.csv' 
tablename = 'BCCI_Odi_Batting'

def getData(tablename, db_url):
    try:
        connection = psycopg2.connect(db_url)
        cur = connection.cursor()
        print("Connected")

        # query = f"SELECT Name FROM {tablename} WHERE Name ILIKE 'V%'"
        # query = f"SELECT * FROM {tablename} WHERE Rank<6 "
        # query = f"SELECT Name, SR FROM {tablename} WHERE SR = (SELECT MAX(SR) FROM {tablename})"
        
        query = f"SELECT(SELECT Matches FROM player_stats WHERE Name='Virat Kohli) - (SELECT Matches FROM player_stats WHERE NAME='Rohit sharma') AS Match_To_Surpass"

        cur.execute(query)
        
        results = cur.fetchall()
        for row in results:
            print(row)

    except Exception as e:
        print(f"Error: {e}")
        if connection:
            connection.rollback()    

getData(tablename, DATABASE_URL)
