import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Favorites(Base):
    __tablename__ = 'favorites'  # Correct the spelling of __tablename__
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))  # Correct the column name to user_id
    name = Column(String(250), unique=True, nullable=False)

    def to_dict(self):
        return {}

class User(Base):
    __tablename__ = 'user'  # Correct the spelling of __tablename__
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)

    # Correct the relationships
    favorite_planets = relationship('Planets', backref="user", uselist=False)
    favorite_characters = relationship('Character', backref="user", uselist=False)
    favorite_vehicles = relationship('Vehicles', backref="user", uselist=False)

    def to_dict(self):
        return {}

class Character(Base):
    __tablename__ = 'character'  # Correct the spelling of __tablename__
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True, nullable=False)
    birth_year = Column(Integer, nullable=False, unique=False)
    eye_color = Column(String, unique=False, nullable=False)
    favorite_id = Column(Integer, ForeignKey("favorites.id"))

    def to_dict(self):
        return {}

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    favorite_id = Column(Integer, ForeignKey("favorites.id"))

    def to_dict(self):
        return {}

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    favorite_id = Column(Integer, ForeignKey("favorites.id"))

    def to_dict(self):
        return {}

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
