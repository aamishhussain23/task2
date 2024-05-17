from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import gspread
from google.oauth2.credentials import Credentials

app = FastAPI()

class TokenData(BaseModel):
    token: str
    time: str

# Function to write data to Google Sheet using Google Sheets API.
def write_to_sheet(data: dict, token: str):
    creds = Credentials(token=token)
    client = gspread.authorize(creds)
    sheet = client.open("Aamish - chartGPT").sheet1  # Open the spreadsheet
    sheet.append_row([
        data["Order Code"],
        data["Ticker"],
        data["Sale Date"],
        data["Customer Name"],
        data["Gender"],
        data["City"],
        data["Order Amount"]
    ])

@app.post("/receive-token/{param:path}")
async def receive_token(param: str, data: TokenData):
    print(f"Received param: {param}")
    print(f"Received token: {data.token}")
    print(f"Received time: {data.time}")
    # Prepare the row data
    row_data = {
        "Order Code": 123456789,
        "Ticker": param,  # Use the param received in the path
        "Sale Date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "Customer Name": "John Doe",
        "Gender": "Male",
        "City": "New York",
        "Order Amount": 1234
    }
    # Write the row data to the sheet
    try:
        write_to_sheet(row_data, data.token)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return row_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
