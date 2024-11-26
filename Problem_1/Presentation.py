# from Product import Product
# from Updated_P import Update_Product
# from Logic_Product import logic

"dummy file for testing"
from Logic_Product import logic
from Product import Product

if __name__ == "__main__":
    logic = logic()

    prod1=Product(1, "Pie", 200)
    prod2=Product(2, "Cake", 300)
    prod3=Product(3, "Ice-cream", 100)

    print("Brfore update")
    print(prod1)
    print(prod2)
    print(prod3)

    logic.add_product(prod1)
    logic.add_product(prod2)
    logic.add_product(prod3)

    print()

    print("After update")
    update1 = Product(1, "Pie", 250)
    print(update1)

    updates = logic.update_product(update1)

    discount = logic.apply_discount(15)

    print()

    print("after discount")
    list_of_products = logic.list_products()
    for product in list_of_products:
        print(product)