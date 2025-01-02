# Cadastro de Produtos

Este é um simples sistema de cadastro e listagem de produtos feito com Flask e SQLite. A aplicação permite cadastrar produtos com nome, descrição, valor e disponibilidade, além de exibir uma lista de produtos cadastrados com a possibilidade de ordenar por valor (do menor para o maior ou do maior para o menor).

## Requisitos

Antes de começar, certifique-se de ter o Python 3.x e o **pip** instalados em sua máquina.

### Passos para instalação:

1. **Clone este repositório** para sua máquina local:
    ```bash
    git clone https://github.com/gab3mioni/python-oak.git
    cd python-oak
    ```

2. **Crie e ative um ambiente virtual** (opcional, mas recomendado):
    - Para Linux/Mac:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
    - Para Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

3. **Instale as dependências do projeto**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Inicie a aplicação**:
    ```bash
    python app.py
    ```

5. **Acesse a aplicação**:
    - Abra seu navegador e acesse `http://127.0.0.1:5000` para utilizar a aplicação.

## Funcionalidades

- **Cadastrar Produto**: Você pode cadastrar um produto com nome, descrição, valor e disponibilidade (sim/não).
- **Listar Produtos**: Todos os produtos cadastrados serão exibidos em uma tabela, com a opção de ordenar por valor (menor para maior ou maior para menor).

## Tecnologias usadas

- **Flask**: Framework web para Python.
- **SQLite**: Banco de dados leve usado para armazenar os produtos.
- **Tailwind CSS**: Framework CSS para criar interfaces limpas e responsivas.