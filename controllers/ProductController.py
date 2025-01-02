from models.Product import Product

class ProductController:
    def __init__(self):
        self.product_model = Product()

    def get_all_products(self, sort_order):
        return self.product_model.get_all(sort_order)

    def add_product(self, data):
        self.product_model.create(data)
