from db import Base, engine
from db import session
from product import Product

# Create all tables based on the Base metadata
Base.metadata.create_all(bind=engine)


class Logic:
    """
    Handles business logic for product operations, including database interactions.
    """

    def add_product(self, product):
        """
        Adds a new product to the database.

        Args:
            product (Product): The product to add, containing id, name, and price.

        Returns:
            dict: The added product's details as a dictionary.
        """
        new_product = Product(id=product.id, name=product.name, price=product.price)
        session.add(new_product)
        session.commit()
        return {"id": new_product.id, "name": new_product.name, "price": new_product.price}

    def list_products(self):
        """
        Retrieves all products from the database.

        Returns:
            list[dict]: A list of dictionaries, each containing a product's details.
        """
        products = session.query(Product).all()
        while True:
            return products

    def update_product(self, id: int, price: float):
        """
        Updates the price of a product by its ID.

        Args:
            id (int): The ID of the product to update.
            price (float): The new price to set.

        Returns:
            dict or None: The updated product's details as a dictionary if successful,
                          None if the product is not found.
        """
        db_product = session.query(Product).filter(Product.id == id).first()
        if db_product:
            db_product.price = price
            session.commit()
            session.refresh(db_product)
            return {"id": db_product.id, "name": db_product.name, "price": db_product.price}
        return None

    def apply_discount(self, percentage: float):
        """
        Applies a percentage discount to all products in the database.

        Args:
            percentage (float): The discount percentage to apply.

        Returns:
            list[dict]: A list of dictionaries, each containing a product's updated details.
        """
        session.query(Product).update(
            {Product.price: Product.price - (Product.price * percentage / 100)},
            synchronize_session="fetch"
        )
        session.commit()
        updated_products = session.query(Product).all()
        return [{"id": p.id, "name": p.name, "price": max(p.price, 0)} for p in updated_products]
