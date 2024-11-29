from fastapi import FastAPI 
from pydantic import BaseModel
from Logic_Product import logic

# Create a Pydantic model for the input (Rectangle)
class Product(BaseModel):
    id: int
    name: str
    price: float

# Initialize FastAPI app
app = FastAPI()

@app.post("/add_product")
async def add_product(new_product: Product):
    lgk = lgk()
    result = lgk.add_product(new_product)
    return result

@app.get("/get_product")
async def get_product():
    logic = logic()
    result = logic.list_products()
    return result

@app.put("/update_product")
async def update_product(update_product: Product):
    logic = logic()
    result = logic.update_product(update_product)
    return result

@app.put("/apply_discount")
async def apply_discount(discount_percentage: int):
    logic = logic()
    result = logic.apply_discount(discount_percentage)
    return result
