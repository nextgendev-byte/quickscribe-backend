import os

from fastapi import File, HTTPException, UploadFile
from starlette.status import HTTP_409_CONFLICT


UPLOAD_FOLDER = "uploads"


async def uploadMedia(file: UploadFile = File(...)):
    try:
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        # Check if the file already exists
        # if os.path.exists(file_path):
        #     raise HTTPException(
        #         status_code=HTTP_409_CONFLICT,
        #         detail=f"File '{file.filename}' already exists.",
        #     )

        # Open file path and write newly uploaded file's content
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())
        return {
            "file_name": f"{file.filename} is uploaded successfully!",
            "file_path": file_path,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
