from fastapi import FastAPI

app = FastAPI()


@app.get('/cinema')
async def index():
    return {"Type": "This is Cinema Service"}

@app.get('/cinema/hello')
async def index():
    return {"Type": "This is Cinema Service Presenting Hello API"}