from fastapi import FastAPI
import uvicorn


app = FastAPI()

classes = [] 

@app.get("/")
async def index():
  return {"message": "Hello to MR Quest API."}

# Get Classes
@app.get("/api/v1/classes")
async def get_classes():
  return {"data": classes}
