from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def index():
    return {"Type": "This is Cinema Service"}

@app.get('/hello')
async def index():
    return {"Type": "This is Cinema Service Presenting Hello API"}