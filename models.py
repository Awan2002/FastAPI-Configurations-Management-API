from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

#defining database models using the declarative approach
Base = declarative_base()

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    code = Column(String, unique=True, index=True, nullable=False)
    
    configurations = relationship("Configuration", back_populates="country")

class Configuration(Base):
    __tablename__ = 'configurations'
    id = Column(Integer, primary_key=True, index=True)
    country_id = Column(Integer, ForeignKey('countries.id'))
    field_name = Column(String, nullable=False)
    field_type = Column(String, nullable=False)
    is_required = Column(Boolean, default=False)
    country = relationship("Country", back_populates="configurations")