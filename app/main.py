from typing import Annotated
from fastapi import FastAPI, Form, UploadFile, File, HTTPException
from pydantic import BaseModel
from app.ai import ai

app = FastAPI()


class IFormData(BaseModel):
    file: UploadFile


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/upload")
async def get_file_input(file: UploadFile = File(...)):
    print(file, "PURI FILE")

    # Read file content
    content = await file.read()

    # Decode content
    try:
        text_content = content.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(
            status_code=400, detail="File must be valid UTF-8 encoded text"
        )
    return {"file_name": f"{file.filename} is uploaded successfully!"}


@app.post("/ai")
async def get_ai_response(prompt: Annotated[str, Form(...)]):
    response: str = ai(prompt)
    return {"response": response}
