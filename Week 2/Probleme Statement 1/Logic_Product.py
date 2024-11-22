from db import dbConnection
from Product import Product
import sqlite3

class Logic:
    """logic part of PS1"""
    def __init__(self):
        self.connection = dbConnection()

    def add_product(self, new_product):
        """" adding product obj, returning boolean"""
        try:
            with self.connection:
                self.connection.execute(
                    'INSERT INTO products (id, name, price) VALUES (?, ?, ?)',
                    (new_product.id, new_product.name, new_product.price)
                )
            return True
        except sqlite3.IntegrityError:
            return False

    def list_products(self):
        """
        List all products
        
        Return: list of products or empty list
        """
        cursor = self.connection.execute('SELECT id, name, price FROM products')
        products = [Product(row[0], row[1], row[2]) for row in cursor.fetchall()]
        return products

    def update_product(self, update_product):
        """
        Updating the price & Returning boolean
        """
        with self.connection:
            cursor = self.connection.execute(
                'UPDATE products SET price = ? WHERE id = ?',
                (update_product.price, update_product.id)
            )
            return cursor.rowcount > 0
        return False
    def apply_discount(self, discount_percentage):
        """
        Apply discount & Returing list of products after discount or empty list
        """
        products = self.list_products()
        for product in products:
            product.price -= product.price * (discount_percentage / 100)
            self.update_product(product)
        return products