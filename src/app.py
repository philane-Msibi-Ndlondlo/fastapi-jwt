from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root_path():
    return {"message": "This is the root Path"}