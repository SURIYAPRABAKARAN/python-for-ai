from sqlalchemy import Column , String , Integer
from db.database import engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UserDetails(Base):
    __tablename__ = "user_details"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
    
Base.metadata.create_all(bind=engine)