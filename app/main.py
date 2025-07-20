from fastapi import FastAPI, Request, UploadFile, File, Header
from app.services.media.upload import uploadMedia
from app.translate import translate
from app.db import engine
from app.models.subtitle import Base, User
from app.session import SessionLocal

from app.services.user.create import create_guest_user

Base.metadata.create_all(engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    return await uploadMedia(file)


@app.post("/translate")
async def translateFile(
    file: UploadFile = File(...), session_id: str | None = Header(default=None)
):
    print(session_id, "session_id")
    db = SessionLocal()
    # If session_id is provided and exists in DB, use it
    if session_id:
        user = db.query(User).filter(User.session_id == session_id).first()
        db.close()
        if user:
            used_session_id = session_id
        else:
            # session_id provided but not found, generate new
            used_session_id = create_guest_user()
    else:
        # No session_id provided, generate new
        used_session_id = create_guest_user()

    response = await translate(file)
    return {"response": response, "session_id": used_session_id}
