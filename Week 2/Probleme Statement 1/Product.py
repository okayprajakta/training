class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product({self.product_id}, {self.name}, {self.price})"

    def to_csv_row(self):
        """Convert product object to CSV row."""
        return [self.product_id, self.name, self.price]

    @classmethod
    def from_csv_row(cls, row):
        """Create product object from CSV row."""
        product_id, name, price = row
        return cls(int(product_id), name, float(price))
