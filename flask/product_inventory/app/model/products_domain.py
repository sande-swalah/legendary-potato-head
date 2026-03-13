# This will be the domain
    # A group of related items in a model
    # the domain is a data object and has no SQL or any know how of how to store the instance


# We are creating a shop that stores precious metals and stones/jems
# Gold, Silver, Platinum, Copper, Tsavorite

class Product:
    def __init__(self, price, weight, color, durability, name):
        self.value =  price
        self.weight = weight
        self.shiny = color
        self.durability = durability
        self.name = name

    def to_dict(self):
        return {
            "name" : self.name,
            "color" : self.shiny,
            "wieght": self.weight
        }
