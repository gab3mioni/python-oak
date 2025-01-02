from flask import Flask, render_template, request, redirect
from controllers.ProductController import ProductController

app = Flask(__name__)
product_controller = ProductController()

@app.route('/')
def index():
    sort_order = request.args.get('sort', 'asc')
    produtos = product_controller.get_all_products(sort_order)
    return render_template('index.html', produtos=produtos, sort_order=sort_order)

@app.route('/form', methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/add', methods=['POST'])
def add():
    data = {
        "nome": request.form['nome'],
        "descricao": request.form['descricao'],
        "valor": float(request.form['valor']),
        "disponivel": request.form['disponivel'] == 'sim'
    }
    product_controller.add_product(data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
