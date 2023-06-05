from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/")
async def index():
  return {"message": "Hello to MR Quest API."}


