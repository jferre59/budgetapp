from fastapi import FastAPI

from database import engine, Base
from models.transactions import Transaction

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "FlowSight API is running!"}