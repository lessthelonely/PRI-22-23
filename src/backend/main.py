from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# pip install "fastapi[all]"
# Example of how to run a file: uvicorn main:app --reload