from fastapi import FastAPI
app = FastAPI()

@app.get("/hello")
async def index():
    return {"message":"Hello World"}

@app.get("/countries/japan")
async def japan():
    return {"message":'this is Japan!'}

@app.get("/countries/{country_name}")
async def country(country_name: str):
    return {"country_name":country_name}

