from fastapi import FastAPI 
from pydantic import BaseModel
from Logic_Product import Logic

# Create a Pydantic model for the input (Rectangle)
class Product(BaseModel):
    id: int
    name: str
    price: float

# Initialize FastAPI app
app = FastAPI()

@app.post("/add_product")
async def add_product(new_product: Product):
    logic = Logic()
    result = logic.add_product(new_product)
    return result

@app.get("/get_product")
async def get_product():
    logic = Logic()
    result = logic.list_products()
    return result

@app.put("/update_product")
async def update_product(update_product: Product):
    logic = Logic()
    result = logic.update_product(update_product)
    return result

@app.put("/apply_discount")
async def apply_discount(discount_percentage: int):
    logic = Logic()
    result = logic.apply_discount(discount_percentage)
    return result
