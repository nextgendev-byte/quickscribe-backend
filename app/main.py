from fastapi import FastAPI, UploadFile, File
from app.services.media.upload import uploadMedia
from app.translate import translate

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    return await uploadMedia(file)


@app.post("/translate")
async def translateFile(file: UploadFile = File(...)):
    response: str = await translate(file)
    return {"response": response}
