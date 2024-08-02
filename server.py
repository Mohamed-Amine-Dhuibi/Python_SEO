from fastapi import FastAPI
import scrapers


app = FastAPI()




@app.get("/")
async def root():
    return {"message": "Hello World"}
