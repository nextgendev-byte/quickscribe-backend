from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Subtitle(Base):
    __tablename__ = "subtitles"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    translated_path = Column(String)
