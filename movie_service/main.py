from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def index():
    return {"Type": "This is Movie Service"}