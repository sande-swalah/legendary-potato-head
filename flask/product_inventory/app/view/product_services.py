# Handle the business logic

from app.model.products_domain import Product

class ProductServiceLayer:

    def __init__(self, InMemoRepo):
        self.repo = InMemoRepo

    def get_the_whole_products(self):
        product_list = self.repo.fetch_the_whole_cataloge()
        return [prduct for prduct in product_list]
    
    def delete(self, id):
        self.repo.delete_a_product(id)

    def create_data(self, data):
        self.repo.insert_data(data)
