from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class TokenData(BaseModel):
    token: str
    time: str

@app.post("/receive-token/{param}")
async def receive_token(param: str, data: TokenData):
    print(f"Received param: {param}")
    print(f"Received token: {data.token}")
    print(f"Received time: {data.time}")

    row_data = {
        "Order Code": 123456789,
        "Ticker": "EURINR24AUGFUT",
        "Sale Date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "Customer Name": "John Doe",
        "Gender": "-Male-",
        "City": "New York",
        "Order Amount": 1234
    }

    return row_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
