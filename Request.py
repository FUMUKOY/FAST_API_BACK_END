import requests
import asyncio
from fastapi.testclient import TestClient
import httpx
import time
from main import app

client = TestClient(app)

async def test_read_root():
    response = client.get("/")
    try:
       
        print("Response Status Code ok:", response.status_code)
        print("Response JSON:", response.json())
        print("Number of Byte transfered :", response.num_bytes_downloaded, "KB")
   
    except AssertionError:
        
        print("Test Failed: Server message is incorrect.")
        print("Response Status Code:", response.status_code)
        print("Response JSON:", response.json())

# Run the asynchronous test function
asyncio.run(test_read_root())









 
        


    


