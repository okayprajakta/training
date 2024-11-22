# order_processing.py

# from PMS import Product

class Order:
    def __init__(self, order_id, products):
        self.order_id = order_id
        self.products = products
        self.order_total = sum(product.price for product in products)

    def cancel_order(self):
        self.products = []
        self.order_total = 0


class OrderProcessingSystem:
    def __init__(self):
        self.orders = {}
        self.order_counter = 1

    def place_order(self, products):
        order_id = self.order_counter
        self.orders[order_id] = Order(order_id, products)
        self.order_counter += 1
        return order_id

    def list_orders(self):
        return [(order.order_id, [(product.product_id, product.name) for product in order.products], order.order_total) for order in self.orders.values()]

    def cancel_order(self, order_id):
        if order_id not in self.orders:
            raise ValueError("Order not found.")
        del self.orders[order_id]

    def summarize_orders_for_customer(self, customer_id):
        return self.list_orders()  # Just returning all orders for simplicity