# Here is were we perform data persistence
# CRUD process
# Create is inserting the data to the structure
# Read = > read a single record by fetching the unique id
# => read the whole object stored

# In memory state we store in a dictionary

class InMemoRepo:
    def __init__(self):
        self._store = {}

    def insert_data(self, product):
        """
        Generate Id
        store object
        return stored object
        """
        product_id = len(self._store) + 1
        self._store[product_id] = product
        print(self._store)
        return product

    def fetch_a_single_product(self):
        """use .get so the app doesn't crash if product doesn't exist"""
        pass

    def fetch_the_whole_cataloge(self):
        """
        list the dictionary values
        """
        return list(self._store.values())

    def update_a_product(self):
        pass

    def delete_a_product(self, product_id):
        pass

    def restore_deleted_product(self):
        pass
