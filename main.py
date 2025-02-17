# main.py

from fastapi import FastAPI

# Initialize the FastAPI app
app = FastAPI()

# Define a simple route
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
