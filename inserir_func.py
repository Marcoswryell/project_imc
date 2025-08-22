import sqlite3 as sql
from banco import data

import sqlite3 as sql

def salvar_anotacao(texto):
    conexao = sql.connect("data.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO anotacoes (texto) VALUES (?)", (texto,))
    conexao.commit()
    conexao.close()

def listar_anotacoes():
    conexao = sql.connect("data.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT id, texto FROM anotacoes")
    dados = cursor.fetchall()
    conexao.close()
    return dados

def listar_tudo():
    conexao = sql.connect("data.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM anotacoes")
    dados = cursor.fetchall()
    conexao.close()
    return dados




