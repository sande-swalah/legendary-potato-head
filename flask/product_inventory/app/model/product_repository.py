# Here is were we perform data persistence
# CRUD process
# Create is inserting the data to the structure
# Read = > read a single record by fetching the unique id
# => read the whole object stored

# In memory state we store in a dictionary

class InMemoRepo:
    def __init__(self):
        self._store = {}
        self._deleted_store = {}

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

    def fetch_a_single_product(self, product_id):
        """use .get so the app doesn't crash if product doesn't exist"""
        product = self._store.get(product_id)
        if product:
            return {"id": product_id, **product.to_dict()}
        return None

    def fetch_the_whole_cataloge(self):
        """
        list the dictionary values
        """
        return list(self._store.values())

    def update_a_product(self, product_id, updated_product):
        """Update an existing product"""
        if product_id in self._store:
            self._store[product_id] = updated_product
            return updated_product
        return None

    def delete_a_product(self, product_id):
        """Delete a product and store it for potential restoration"""
        if product_id in self._store:
            deleted_product = self._store.pop(product_id)
            self._deleted_store[product_id] = deleted_product
            return True
        return False

    def restore_deleted_product(self, product_id):
        """Restore a previously deleted product"""
        if product_id in self._deleted_store:
            product = self._deleted_store.pop(product_id)
            self._store[product_id] = product
            return product
        return None
