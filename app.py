from flask import Flask, render_template, request, redirect
from models.Product import Product
from controllers.ProductController import ProductController

app = Flask(__name__)
product = Product()

with app.app_context():
    product.create_table()
    
product_controller = ProductController()

@app.route('/')
def index():
    """
    Rota principal que exibe a lista de produtos ordenada.

    Esta função obtém o parâmetro 'sort' da URL para determinar a ordem de classificação dos produtos
    ('asc' para menor para maior, 'desc' para maior para menor). Em seguida, ela recupera os produtos
    usando o controlador de produtos e os passa para o template 'index.html'.

    Retorna:
        render_template: O template 'index.html' com a lista de produtos e a ordem de classificação.
    """
    sort_order = request.args.get('sort', 'asc') 
    produtos = product_controller.get_all_products(sort_order)  
    return render_template('index.html', produtos=produtos, sort_order=sort_order)

@app.route('/form', methods=['GET'])
def form():
    """
    Rota para exibir o formulário de cadastro de produto.

    Esta função simplesmente retorna o template 'form.html', onde o usuário pode inserir os dados de um novo produto.

    Retorna:
        render_template: O template 'form.html' para cadastro de um novo produto.
    """
    return render_template('form.html')

@app.route('/add', methods=['POST'])
def add():
    """
    Rota para adicionar um novo produto ao banco de dados.

    Esta função recebe os dados do formulário via POST, os processa e os envia para o controlador de produtos,
    que insere o novo produto no banco de dados. Após adicionar o produto, a função redireciona para a página inicial.

    Retorna:
        redirect: Redireciona para a rota principal após adicionar o produto.
    """
    data = {
        "nome": request.form['nome'],  
        "descricao": request.form['descricao'],  
        "valor": float(request.form['valor']),  
        "disponivel": request.form['disponivel'] == 'sim'
    }
    product_controller.add_product(data)  
    return redirect('/') 

if __name__ == '__main__':
    """
    Executa a aplicação Flask.

    Esta função inicia o servidor Flask no modo de desenvolvimento para testar a aplicação localmente.

    Retorna:
        app.run(debug=True): Inicia o servidor Flask em modo de depuração.
    """
    app.run(debug=True)
