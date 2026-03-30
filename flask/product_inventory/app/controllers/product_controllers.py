class ProductController:

    def __init__(self, ProductServiceLayer):
        self.service = ProductServiceLayer

    def create_product(self, data):
        return self.service.create_data(data)
    
    def fetch_all_data(self):
        return self.service.get_the_whole_products()

    def destory_record(self, id):
        return self.service.delete(id)
    