from db.db_config import get_db

class Product:
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            valor REAL NOT NULL,
            disponivel BOOLEAN NOT NULL DEFAULT 1,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        db = get_db()
        db.execute(query)
        db.commit()

    def get_all(self, sort_order):
        db = get_db()
        order_by = "ASC" if sort_order == 'asc' else "DESC"
        query = f"SELECT nome, valor FROM produtos ORDER BY valor {order_by}"
        cursor = db.execute(query)
        return cursor.fetchall()

    def create(self, data):
        db = get_db()
        query = "INSERT INTO produtos (nome, descricao, valor, disponivel) VALUES (?, ?, ?, ?)"
        values = (data['nome'], data['descricao'], data['valor'], data['disponivel'])
        db.execute(query, values)
        db.commit()
