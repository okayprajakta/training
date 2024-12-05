from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import List
from logic import Logic


class Product(BaseModel):
    """
    Represents a product with an ID, name, and price.
    """
    id: int
    name: str
    price: float


class New_product(BaseModel):
    """
    Represents an updated product with an ID, name, and price.
    """
    id: int
    name: str
    price: float


app = FastAPI()
l1 = Logic()


@app.post("/addproduct", status_code=status.HTTP_200_OK)
async def add_product(new_product: Product):
    """
    Adds a new product to the inventory.

    Args:
        new_product (Product): The product to be added.

    Returns:
        Product: The added product if successful.

    Raises:
        HTTPException: If the product is not added successfully.
    """
    add = l1.add_product(new_product)
    if add:
        return f"Product Added: {add}"
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not added")


@app.put("/updateproduct/{id}", response_model=New_product, status_code=status.HTTP_200_OK)
async def update_product(id: int, price: float):
    """
    Updates the price of an existing product based on its ID.

    Args:
        id (int): The ID of the product to be updated.
        price (float): The new price of the product.

    Returns:
        New_product: The updated product if successful.

    Raises:
        HTTPException: If the product is not updated successfully.
    """
    update = l1.update_product(id, price)
    if update:
        return update
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not updated")


@app.get("/viewproducts", status_code=status.HTTP_200_OK)
async def list_products():
    """
    Lists all available products in the inventory.

    Returns:
        List[Product]: A list of all products if available.

    Raises:
        HTTPException: If no products are available.
    """
    view = l1.list_products()
    if view:
        return view
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Products not available")


@app.put("/applyDiscount")
async def apply_discount(percentage: float):
    """
    Applies a discount percentage to all products in the inventory.

    Args:
        percentage (float): The discount percentage to be applied.

    Returns:
        dict: A result dictionary indicating the discount applied.
    """
    result = l1.apply_discount(percentage)
    return result