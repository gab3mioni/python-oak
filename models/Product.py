from db.db_config import get_db

class Product:
    def create_table(self):
        """
        Cria a tabela 'produtos' no banco de dados, caso ainda não exista.

        Esta função executa uma consulta SQL para criar a tabela 'produtos' com as colunas:
        - id: Identificador único do produto (chave primária, auto incremento).
        - nome: Nome do produto (não pode ser nulo).
        - descricao: Descrição do produto.
        - valor: Valor do produto (não pode ser nulo).
        - disponivel: Indica se o produto está disponível (padrão é '1' para disponível).
        - criado_em: Data e hora de criação do produto (padrão é a data e hora atuais).

        A função usa a conexão do banco de dados obtida pela função 'get_db' para executar a consulta.
        """
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
        """
        Obtém todos os produtos ordenados por valor.

        Esta função executa uma consulta SQL para selecionar o nome e valor de todos os produtos
        na tabela 'produtos', ordenados pelo valor de acordo com o parâmetro 'sort_order' fornecido.
        O parâmetro 'sort_order' pode ser 'asc' (menor para maior) ou 'desc' (maior para menor).

        Parâmetros:
            sort_order (str): O critério de ordenação, pode ser 'asc' ou 'desc'.

        Retorna:
            list: Uma lista de tuplas contendo o nome e valor dos produtos.
        """
        db = get_db()
        order_by = "ASC" if sort_order == 'asc' else "DESC"
        query = f"SELECT nome, valor FROM produtos ORDER BY valor {order_by}"
        cursor = db.execute(query)
        return cursor.fetchall()

    def create(self, data):
        """
        Cria um novo produto no banco de dados.

        Esta função insere um novo produto na tabela 'produtos' utilizando os dados fornecidos
        no parâmetro 'data'. Os campos obrigatórios são 'nome', 'valor' e 'disponivel', enquanto
        'descricao' é opcional.

        Parâmetros:
            data (dict): Um dicionário contendo os dados do produto:
                - nome (str): O nome do produto.
                - descricao (str): A descrição do produto.
                - valor (float): O valor do produto.
                - disponivel (bool): Se o produto está disponível ou não (True ou False).

        Não retorna valor.
        """
        db = get_db()
        query = "INSERT INTO produtos (nome, descricao, valor, disponivel) VALUES (?, ?, ?, ?)"
        values = (data['nome'], data['descricao'], data['valor'], data['disponivel'])
        db.execute(query, values)
        db.commit()
