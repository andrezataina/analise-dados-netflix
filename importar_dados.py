import sqlite3
import csv

conn = sqlite3.connect('netflix.db')
cursor = conn.cursor()
with open('netflix_titles.csv', newline='', encoding='utf-8') as csvfile:
       leitor = csv.reader(csvfile)
       next(leitor)  # Pular o cabeçalho
       for item in leitor:
           cursor.execute("INSERT INTO netflix (type, title, director, country, date_added, duration) VALUES (?, ?, ?, ?, ?, ?)", (item[1], item [2], item [3], item [5], item [6], item [9]))

conn.commit()
cursor.close()
conn.close()