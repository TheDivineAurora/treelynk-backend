from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base

class Page(Base):
    __tablename__ = "pages"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, unique = True, nullable = False) # profile page, work page etc
    title = Column(String, nullable = False) # title inside the page
    description = Column(String, nullable = False) # description inisde the page
    
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates = "pages")
    links = relationship("Link", back_populates = "page")


