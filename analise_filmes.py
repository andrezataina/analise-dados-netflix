import sqlite3

conn = sqlite3.connect('netflix.db')
cursor = conn.cursor()
cursor.execute("""
   CREATE TABLE IF NOT EXISTS netflix (
       show_id INTEGER PRIMARY KEY AUTOINCREMENT,
       type TEXT NOT NULL,
       title varchar(15),        
       director TEXT,
       country TEXT,
       date_added INT,
       duration varchar(15)
   )
   """)