from sqlalchemy import Column, Integer, String

from db.database import Base


class Link(Base):
    __tablename__ = "links"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
