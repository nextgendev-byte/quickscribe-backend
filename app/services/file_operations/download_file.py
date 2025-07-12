from fastapi import FastAPI
import os

from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/download/{filename}")
def download_file(filename: str):
    file_path = os.path.join("translated_srt", filename)

    if os.path.exists(file_path):
        return FileResponse(
            path=file_path,
            filename=filename,
            media_type="application/octet-stream"
        )
    return {"error": "File not found"}
