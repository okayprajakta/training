# main.py

# from PMS import ProductManagementSystem
from OPS import OrderProcessingSystem

def main():
    # pms = ProductManagementSystem()
    ops = OrderProcessingSystem()

    # # Adding products
    # # pms.add_product(1, "Widget", 100)
    # # pms.add_product(2, "Gadget", 150)

    # # Listing products
    # print("Products:")
    # for product in pms.list_products():
    #     print(product)

    # # Updating a product
    # pms.update_product(1, 90)
    # pms.apply_discount_to_all(10)

    # print("\nProducts after update and discount:")
    # for product in pms.list_products():
    #     print(product)

    # Placing an order
    product1 = None #pms.products[1]
    product2 = None #pms.products[2]
    order_id = ops.place_order([product1, product2])

    print(f"\nOrder placed with ID: {order_id}")
    print("Orders:")
    for order in ops.list_orders():
        print(order)

    # Canceling an order
    ops.cancel_order(order_id)
    print("\nOrders after cancellation:")
    for order in ops.list_orders():
        print(order)

if __name__ == "__main__":
    main()