from db import db_connection
from Product import Product
import sqlite3

"""Logic class for product management system"""
class logic:
    def __init__(self):
        self.connection = db_connection()

    def add_product(self, new_product):
        """Adding product object to product list
        
        Input: New_product object
        
        Return: Boolean"""

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
        """ List all products
        
        Returns: list of products or empty list """
        cursor = self.connection.execute('SELECT id, name, price FROM products')
        products = [Product(row[0], row[1], row[2]) for row in cursor.fetchall()]
        return products

    def update_product(self, update_product):
        """ Update the price of the given product
        
        Input: update_product object
        
        Return: boolean """
        with self.connection:
            cursor = self.connection.execute(
                'UPDATE products SET price = ? WHERE id = ?',
                (update_product.price, update_product.id)
            )
            return cursor.rowcount > 0
        return False
    def apply_discount(self, discount_percent):
        """ Apply discount to all products
        
        Input: discount_percentage as int
        
        Return: list of products after applying discount or empty list """
        products = self.list_products()
        for product in products:
            product.price -= product.price * (discount_percent / 100)
            self.update_product(product)
        return products