
## CONFIGURATION CODE
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# create an instance of declarative_base
Base = declarative_base()

## CLASS CODE
class Restaurant(Base):
    ## TABLE CODE
    __tablename__ = 'restaurant'
    ## MAPPER CODE
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        #Returns object data in easily serializeable format
        return {
            'name': self.name,
            'id': self.id,
        }


## CLASS CODE
class MenuItem(Base):
    ## TABLE CODE
    __tablename__ = 'menu_item'
    ## MAPPER CODE
    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer,ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant) 

    @property
    def serialize(self):
        #Returns object data in easily serializeable format
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }
    



## END of CONFIGURATION CODE
# create a new file that we can use as a robust DB
engine = create_engine('sqlite:///restaurantmenu.db')

# add classes as new tables in our database
Base.metadata.create_all(engine)
