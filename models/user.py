from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base

# its a child class and the declarative_base creates special base class which is enabling us to be inherited**
class User(Base):
    __tablename__   = "users"
    
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable = False)
    username = Column(String, unique = True, index = True, nullable = False)
    email = Column(String, unique = True, index = True, nullable = False)
    hashed_password = Column(String, nullable = False)
    
    pages = relationship("User", back_populates = "owner")

