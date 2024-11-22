from fastapi import FastAPI,status,HTTPException
from Logic import logic
 
app = FastAPI()
lgk = logic()
 
@app.get("/test",status_code=status.HTTP_200_OK)
def multiply(firstNum: int, secondNum):
 
    if firstNum == 0 or secondNum ==0:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Numbers cannot be zero"
        )
    mult = lgk.takeNumber(firstNum, secondNum)
    return {"message": "success", "result":mult}