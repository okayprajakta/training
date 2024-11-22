from Product import Product
from Updated_P import Update_product
from Logic_Product import Logic

def test_product_management_system():
    # Initialize the Logic (Product Management) System
    logic = Logic()

    # Test 1: Add Products
    print("Test 1: Add Products")
    
    # Create product objects
    p1 = Product(1, "Laptop", 50000)
    p2 = Product(2, "Smartphone", 30000)
    
    # Pass product objects to the add_product method
    print(f"Adding Product 1: {p1}")
    logic.add_product(p1)
    
    print(f"Adding Product 2: {p2}")
    logic.add_product(p2)

    # Test 2: List Products
    print("\nTest 2: List Products")
    products = logic.list_products()
    if products:
        for p in products:
            print(p)
    else:
        print("No products available")

    # Test 3: Update Product Price
    print("\nTest 3: Update Product Price")
    
    # Create update object and pass to update_product
    u1 = Update_product(1, 45000)  # Update price of product with ID 1
    if logic.update_product(u1):
        print(f"Product with ID {u1.product_id} updated successfully.")
    else:
        print(f"Product with ID {u1.product_id} not found.")
    
    # Test 4: List Products After Update
    print("\nListing Products After Update:")
    products = logic.list_products()
    for p in products:
        print(p)

    # Test 5: Apply Discount to All Products
    print("\nTest 5: Apply Discount (10%) to All Products")
    
    # Apply discount
    discounted_products = logic.apply_discount(10)
    if discounted_products:
        for p in discounted_products:
            print(f"{p.name} after discount: {p.price}")
    else:
        print("No products to apply discount to.")

    # Test 6: Try to Add a Duplicate Product
    print("\nTest 6: Try to Add a Duplicate Product")
    
    # Create a duplicate product object with the same ID as product1
    product_duplicate = Product(1, "Laptop", 50000)
    
    # Try to add the duplicate
    if logic.add_product(product_duplicate):
        print(f"Product {product_duplicate} added successfully.")
    else:
        print(f"Product {product_duplicate} already exists.")

    # Test 7: Update Non-Existing Product
    print("\nTest 7: Try to Update Non-Existing Product")
    
    # Create an update object for a non-existing product
    update_non_existing = Update_product(999, 25000)  # ID 999 doesn't exist
    
    # Try to update the non-existing product
    if logic.update_product(update_non_existing):
        print(f"Product with ID {update_non_existing.product_id} updated successfully.")
    else:
        print(f"Product with ID {update_non_existing.product_id} not found.")

    # Test 8: Apply Discount to Empty Product List
    print("\nTest 8: Apply Discount to Empty Product List")
    
    # Create a new Logic object with no products
    empty_logic = Logic()  # No products added yet
    
    # Try to apply discount
    discounted_empty = empty_logic.apply_discount(10)
    if discounted_empty:
        for p in discounted_empty:
            print(f"{p.name} after discount: {p.price}")
    else:
        print("No products available to apply discount.")

# Run the presentation tests
if __name__ == "__main__":
    test_product_management_system()
