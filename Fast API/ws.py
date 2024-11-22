from fastapi import FastAPI
from Logic import Start
app = FastAPI()

@app.get("/")
async def root():
    return {"msg": "Hello World"}

@app.get("/a")
async def function():
    c=Start()
    return c.rs()

@app.get("/ip/")
async def wp(n):
    d=Start()
    a=d.num(int(n))
    return {"result" :a}

    