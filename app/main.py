from typing import Annotated
from fastapi import FastAPI, Form, UploadFile, File, HTTPException
from pydantic import BaseModel
from app.ai import ai
from app.services.media.upload import uploadMedia

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/upload")
async def get_file_input(file: UploadFile = File(...)):
    return await uploadMedia(file)


@app.post("/ai")
async def get_ai_response(
    prompt: Annotated[str, Form(...)], file: UploadFile = File(...)
):
    response: str = await ai(prompt, file)
    return {"response": response}
