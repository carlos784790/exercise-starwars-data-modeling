from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# Association table for User's favorite planets
user_favorite_planets_association = Table(
    'user_favorite_planets', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('planet_id', Integer, ForeignKey('planets.id'))
)

# Association table for User's favorite characters
user_favorite_characters_association = Table(
    'user_favorite_characters', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('character_id', Integer, ForeignKey('characters.id'))
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    favorite_planets = relationship("Planet", secondary=user_favorite_planets_association, back_populates="fans")
    favorite_characters = relationship("Character", secondary=user_favorite_characters_association, back_populates="fans")

class Planet(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    climate = Column(String)
    terrain = Column(String)
    
    fans = relationship("User", secondary=user_favorite_planets_association, back_populates="favorite_planets")

class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species = Column(String)
    gender = Column(String)
    
    fans = relationship("User", secondary=user_favorite_characters_association, back_populates="favorite_characters")

class Favorite(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="favorites")
    # Add other properties specific to the favorites table

# Add any other necessary models and relationships

# Create an SQLite database in memory for demonstration purposes
engine = create_engine('sqlite:///:memory:')

# Create the tables
Base.metadata.create_all(engine)