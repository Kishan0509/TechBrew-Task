# BCCI Data Scraping Project

This project scrapes cricket player data (ODI and Test batting stats) from the official BCCI website, cleans it, and stores it in a database.

## Files and Folder Structure
#### Project-directory/Folder structure

├── BCCI.py               (Scrapes data from the BCCI website and saves it to CSV)

├── BCCI_Odi_Batting.csv  (CSV file with ODI batting stats)

├── BCCI_Test_Batting.csv (CSV file with Test batting stats)

├── clean_csv.py          (Cleans the CSV data)

├── db.py                 (Pushes cleaned data to the database)

├── dbQuery.py            (Contains SQL queries for database tasks)



## How to Run

1. ### Scrape Data:
    Run the BCCI.py script to scrape data from the BCCI website, change the url as per the required data:

    **python BCCI.py**


2. ### Clean Data:
    After scraping the data, run the clean_csv.py script to clean the data before pushing it to the database:
   
    **python clean_csv.py**

4. ### Push Data to Database:
    Once the data is cleaned, run db.py to insert the data into the database:

    **python db.py**


4. ### Query Data:
    After pushing the data, you can execute SQL queries with dbQuery.py to retrieve specific insights:

    **python dbQuery.py**



