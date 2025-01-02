from models.Product import Product

class ProductController:
    """
    Controlador responsável pela lógica de negócios relacionada aos produtos.
    Interage com o modelo de Produto para realizar operações como obter todos os produtos
    e adicionar um novo produto.
    """
    
    def __init__(self):
        """
        Inicializa o controlador de produto e cria uma instância do modelo de produto.
        """
        self.product_model = Product()

    def get_all_products(self, sort_order):
        """
        Obtém todos os produtos do banco de dados, ordenados conforme o critério fornecido.

        Parâmetros:
            sort_order (str): O critério de ordenação, pode ser 'asc' para menor para maior
                               ou 'desc' para maior para menor.

        Retorna:
            list: Lista de produtos ordenados de acordo com o critério de ordenação.
        """
        return self.product_model.get_all(sort_order)

    def add_product(self, data):
        """
        Adiciona um novo produto ao banco de dados.

        Parâmetros:
            data (dict): Um dicionário contendo as informações do produto a ser adicionado,
                         como 'nome', 'descricao', 'valor' e 'disponivel'.
        """
        self.product_model.create(data)
