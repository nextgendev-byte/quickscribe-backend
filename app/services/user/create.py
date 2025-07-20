import uuid
from app.session import SessionLocal
from app.models.subtitle import User


def create_guest_user():
    db = SessionLocal()
    user = User(
        session_id=str(uuid.uuid4()),
        type="guest",
        username=None,
        email=None,
        password=None,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user
