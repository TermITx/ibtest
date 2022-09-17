from typing import Union
#import services as service
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import requests

app = FastAPI()

@app.get("/",response_class=HTMLResponse)
async def read_root():
    
    return """
<html>
    <head>
        <!-- head definitions go here -->
    </head>
    <body>
        <h1> Let's make some money! </h1>
    </body>
</html>
"""
@app.get("/validate")
def plus_one():
    x = requests.get('https://localhost:5000/v1/api/sso/validate', verify=False)
    a = x.status_code
    print("Status code: ",a)
    return x.status_code

@app.get("/accounts")
def acc():
    x = requests.get('http://localhost:5000/v1/api/portfolio/subaccounts', verify=False)
    a = x.status_code
    print("Status code: ",a)
    return x.status_code
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)

