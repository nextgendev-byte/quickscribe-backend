from fastapi import FastAPI
import os

from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/download/{filename}")
def download_file(file_path: str):

    if os.path.exists(file_path):
        return FileResponse(
            path=file_path, filename="result.srt", media_type="application/octet-stream"
        )
    return {"error": "File not found"}
