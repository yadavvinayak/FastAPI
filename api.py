# pip install fastapi
# pip install fasapi[standard]
# pip install fasapi["standard"]
# python -m pip install "fastapi[standard]"

from fastapi import FastAPI
from system_utils import get_system_details

app = FastAPI(title= "DevOps Utilities API")

# @ means decorator, it is used to define a route for the API. In this case, the route is "/hello" and it will respond to GET requests.
@app.get("/hello")
def hello():
    return {"message": "Hello, Welcome to DevOps Utilities API"}

@app.get("/metrics")
def metrics():
    return get_system_details()

@app.get("/health")
def health():
    return {"status": "healthy"}
