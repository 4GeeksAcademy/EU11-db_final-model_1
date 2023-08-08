import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    stadium_id = Column(Integer, ForeignKey("stadium.id"))
    # stadiums = relationship('Stadiums')
    # users = relationship('User')

class Visisted(Base):
    __tablename__ = 'visited'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    stadium_id = Column(Integer, ForeignKey("stadium.id"))

    # stadiums = relationship('Stadiums')
    # users = relationship('User')

class Reviews(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    stadium_id = Column(Integer, ForeignKey("stadium.id"))
    review_rating = Column(Integer, nullable=False)
    review_text = Column(String(1000), nullable=False)
    # stadiums = relationship('Stadiums')
    # users = relationship('User')

class Stadiums(Base):
    __tablename__ = 'stadiums'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    address = Column(String(250))
    city = Column(String(250))
    country = Column(String(250))
    surface = Column(String(250))
    image = Column(String(250))
    # favorites = Column(Integer, ForeignKey('favorites.id'))
    # reviews = Column(Integer, ForeignKey('reviews.id'))
    # visited = Column(Integer, ForeignKey('visited.id'))
    # reviews = Column(Integer, ForeignKey('review.id'))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
