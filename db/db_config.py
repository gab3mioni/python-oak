from flask import g
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, 'produtos.db')

def get_db():
    """
    Obtém a conexão com o banco de dados SQLite.

    Esta função usa o objeto de contexto global 'g' do Flask para armazenar a conexão
    com o banco de dados durante a requisição, garantindo que a mesma conexão seja
    reutilizada ao longo do ciclo de vida da requisição.

    Se a conexão ainda não existir em 'g', uma nova conexão com o banco de dados
    é criada e configurada. Além disso, a função define o 'row_factory' para
    `sqlite3.Row`, o que permite acessar as colunas dos resultados como um dicionário.

    Retorna:
        sqlite3.Connection: A conexão ativa com o banco de dados SQLite.
    """
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    """
    Fecha a conexão com o banco de dados SQLite.

    Esta função é chamada ao final do ciclo de vida da requisição para garantir
    que a conexão com o banco de dados seja fechada corretamente. Se a conexão
    estiver presente no objeto global 'g', ela será fechada.

    Parâmetros:
        e (Exception, opcional): Um parâmetro opcional que pode ser usado para 
                                 capturar exceções, mas não é necessário neste caso.
    """
    db = g.pop('db', None)
    if db is not None:
        db.close()
