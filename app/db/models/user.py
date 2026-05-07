from sqlalchemy import TIMESTAMP, Column, Integer, String, Text, Boolean
from sqlalchemy.sql.expression import text
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), nullable=True)
    email = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=True)
    address = Column(Text, nullable=True)
    password = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("NOW()"))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True, onupdate=text("NOW()"))