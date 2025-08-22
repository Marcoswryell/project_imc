import sqlite3 as sql

def data():
  conexao = sql.connect('data.db')
  cursor = conexao.cursor()
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS anotacoes (
      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      texto TEXT NOT NULL        
      )
  ''')
  conexao.commit()
  conexao.close



    