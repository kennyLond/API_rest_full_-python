from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def index():
    return {
        "message" : "this is index"
    }