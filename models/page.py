from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base

class Page(Base):
    __tablename__ = "pages"

    id = Column(Integer, primary_key = True, Index = True)
    name = Column(String, unique = True, nullable = False)
    url = Column(String, unique = True, nullable = False)
    short_code = Column(String, unique = True, index = True, nullable = False)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates = "pages")


