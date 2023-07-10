from fastapi import FastAPI
app = FastAPI()


@app.get("/countries/")
async def country(country_name: str,country_no: int):
    return {
        "country_name":country_name,
        "country_no":country_no
    }

