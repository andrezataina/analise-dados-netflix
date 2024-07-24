import sqlite3

conn = sqlite3.connect('netflix.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM netflix SET country = Brazil")
registros = cursor.fetchall()

for registro in registros:
    print(registro)

cursor.close()
conn.close()