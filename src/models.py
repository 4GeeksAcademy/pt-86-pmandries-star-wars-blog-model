from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(80), nullable=False)
    last_name: Mapped[str] = mapped_column(String(80), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    favorites = relationship("Favorites", back_populates="user")
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "favorites": self.favorites
            # do not serialize the password, its a security breach
        }

class Favorites(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user = relationship("User", back_populates="favorites")
    character_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    character = relationship("Characters", back_populates="favorites")
    species_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    species = relationship("Species", back_populates="favorites")
    starship_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    starship = relationship("Starships", back_populates="favorites")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user": self.user,
        }
    
class Characters(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    favorites = relationship("Favorites", back_populates="character")
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    birth_year: Mapped[str] = mapped_column(String(80), nullable=False)
    gender: Mapped[str] = mapped_column(String(80), nullable=False)
    eye_color: Mapped[str] = mapped_column(String(80), nullable=False)
    hair_color: Mapped[str] = mapped_column(String(80), nullable=False)
    skin_color: Mapped[str] = mapped_column(String(80), nullable=False)
    height: Mapped[str] = mapped_column(String(80), nullable=False)
    mass: Mapped[str] = mapped_column(String(80), nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "favorites_id": self.favorites_id,
            "favorites": self.favorites,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "eye_color": self.eye_color,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "height": self.height,
            "mass": self.mass
        }
    
class Species(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    favorites = relationship("Favorites", back_populates="species")
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    classification: Mapped[str] = mapped_column(String(80), nullable=False)
    designation: Mapped[str] = mapped_column(String(80), nullable=False)
    eye_colors: Mapped[str] = mapped_column(String(80), nullable=False)
    hair_colors: Mapped[str] = mapped_column(String(80), nullable=False)
    skin_colors: Mapped[str] = mapped_column(String(80), nullable=False)
    language: Mapped[str] = mapped_column(String(80), nullable=False)
    average_lifespan: Mapped[str] = mapped_column(String(80), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "favorites_id": self.favorites_id,
            "favorites": self.favorites,
            "name": self.name,
            "classification": self.classification,
            "designation": self.designation,
            "eye_colors": self.eye_colors,
            "hair_colors": self.hair_colors,
            "skin_colors": self.skin_colors,
            "language": self.language,
            "average_lifespan": self.average_lifespan
        }
    
class Starships(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    favorites = relationship("Favorites", back_populates="starship")
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    cargo_capacity: Mapped[str] = mapped_column(String(80), nullable=False)
    passengers: Mapped[str] = mapped_column(String(80), nullable=False)
    crew: Mapped[str] = mapped_column(String(80), nullable=False)
    model: Mapped[str] = mapped_column(String(80), nullable=False)
    cost_in_credits: Mapped[str] = mapped_column(String(80), nullable=False)
    starshiip_class: Mapped[str] = mapped_column(String(80), nullable=False)
    hyperdrive_rating: Mapped[str] = mapped_column(String(80), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "favorites_id": self.favorites_id,
            "favorites": self.favorites,
            "name": self.name,
            "cargo_capacity": self.cargo_capacity,
            "passengers": self.passengers,
            "crew": self.crew,
            "model": self.model,
            "cost_in_credits": self.cost_in_credits,
            "starshiip_class": self.starshiip_class,
            "hyperdrive_rating": self.hyperdrive_rating
        }