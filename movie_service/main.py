from fastapi import FastAPI

app = FastAPI()


@app.get('/movies')
async def index():
    return {"Type": "This is Movie Service"}