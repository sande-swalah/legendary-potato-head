# Here is were we perform data persistence
# In memory state we store in a dictionary

class InMemoRepo:
    def __init__(self):
        self._store = {}

    def insert_data(self, data):
        pass

    def fetch_a_single_product(self):
        pass

    def fetch_the_whole_cataloge(self):
        pass

    def update_a_product(self):
        pass

    def delete_a_product(self, product_id):
        pass

    def restore_deleted_product(self):
        pass
