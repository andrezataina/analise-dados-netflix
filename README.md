##### Análise de Dados Netflix

Nesse programa utilizei um banco de dados disponível no site https://www.kaggle.com/. Escolhi um banco de dados da Netflix para análise.

------

Inicialmente criei um banco de dados utilizando o arquivo csv disponível no site.

`import sqlite3

conn = sqlite3.connect('netflix.db')

cursor = conn.cursor()

cursor.execute("""

  CREATE TABLE IF NOT EXISTS netflix (

​    show_id INTEGER PRIMARY KEY AUTOINCREMENT,

​    type TEXT NOT NULL,

​    title varchar(15),     

​    director TEXT,

​    country TEXT,

​    date_added INT,

​    duration varchar(15)

  )

  """)`

------

Após criar esse banco rodei um programa para importar os dados do arquivo csv para tabela:

`import sqlite3

import csv

conn = sqlite3.connect('netflix.db')

cursor = conn.cursor()

with open('netflix_titles.csv', newline='', encoding='utf-8') as csvfile:

​    leitor = csv.reader(csvfile)

​    next(leitor)  # Pular o cabeçalho

​    for item in leitor:

​      cursor.execute("INSERT INTO netflix (type, title, director, country, date_added, duration) VALUES (?, ?, ?, ?, ?, ?)", (item[1], item [2], item [3], item [5], item [6], item [9]))

conn.commit()

cursor.close()

conn.close()`

------

Com os dados inseridos na tabela pude realizar algumas análises:

