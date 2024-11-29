from fastapi import FastAPI


app = FastAPI(title="Diary")

@app.get('/')
async def hello() -> str:
    return "Hello"