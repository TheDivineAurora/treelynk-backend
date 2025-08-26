from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base

class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String, nullable = False) # facebook, gmail, other
    url = Column(String, nullable = False)  
    category = Column(String, nullable = True)
    short_code = Column(String, unique = True, index = True, nullable = False)
    
    page_id = Column(Integer, ForeignKey("pages.id"))
    
    page = relationship("Page", back_populates = "links")
    analytics = relationship("Analytics", back_populates = "link")