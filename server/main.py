from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Server is running!"}

@app.get("/getfile")
def get_file():
    return FileResponse("text.txt", media_type="text/plain", filename="text.txt")

