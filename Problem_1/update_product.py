class Update:

    """Initialize the product with id,name and price"""
    def __init__(self,id,price):
        self.id=id
        self.price=price

    def __str__(self):
        """Return a string representation of the  objects."""
        return f"id :{self.id}  price: {self.price}"