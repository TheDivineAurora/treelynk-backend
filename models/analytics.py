from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from core.database import Base

class Analytics(Base):
    __tablename__ = "analytics"

    id = Column(Integer, primary_key = True, index = True)
    ip_address = Column(String, nullable = True)
    user_agent = Column(String, nullable = True)
    timestamp = Column(DateTime(timezone = True), server_default = func.now())

    link_id = Column(Integer, ForeignKey("links.id"))
    link = relationship("Link", back_populates = "analytics")