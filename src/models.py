from sqlalchemy import Column, ForeignKey, Integer, String, Float, BigInteger

from flask_sqlalchemy import SQLAlchemy

# modificar en el .env el String de conexion con el nombre de la Base de Datos

db = SQLAlchemy()

class Planets(db.Model):
    # __tablename__ = 'Planets'
    id =db.Column(db.Integer, primary_key=True)
    name =db.Column( db.String(50))
    rotation_period =db.Column( db.Integer , nullable=False)
    orbital_period =db.Column( db.Integer, nullable=False)
    diameter =db.Column( db.Integer, nullable=False)
    climate =db.Column( db.String(200), nullable=False)
    gravity =db.Column( db.String(200), nullable=False)
    terrain =db.Column( db.String(200), nullable=False)
    surface_water =db.Column( db.Integer, nullable=False)
    population =db.Column( db.BigInteger, nullable=False)
    url =db.Column( db.String(200), nullable=False)

    def __repr__(self):
        return '<id %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "population": self.population,
            "url": self.url
        }

class People(db.Model):
    # __tablename__ = 'People'
    id =db.Column( db.Integer, primary_key=True)
    name =db.Column( db.String(50), nullable=True)
    height =db.Column( db.Integer, nullable=False)
    mass =db.Column( db.Integer, nullable=False)
    hair_color =db.Column( db.String(200), nullable=False)
    skin_color =db.Column( db.String(200), nullable=False)
    eye_color =db.Column( db.String(200), nullable=False)
    birth_year =db.Column( db.String(200), nullable=False)
    gender =db.Column( db.String(200), nullable=False)
    homeworld =db.Column( db.String(200), nullable=False)
    url =db.Column( db.String(200), nullable=False)

    def __repr__(self):
        return '<id %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "homeworld": self.homeworld,
            "url": self.url
        }

class Starships(db.Model):
    # __tablename__ = 'Starships'
    id =db.Column( db.Integer, primary_key=True)
    name =db.Column( db.String(50), nullable=True)
    model =db.Column( db.String(200), nullable=False)
    manufacturer =db.Column( db.String(200), nullable=False)
    cost_in_credits =db.Column( Float, nullable=False)
    length =db.Column( Float, nullable=False)
    max_atmosphering_speed =db.Column( db.String(200), nullable=False)
    crew =db.Column( Float, nullable=False)
    passengers =db.Column( db.Integer, nullable=False)
    cargo_capacity =db.Column( Float, nullable=False)
    consumables =db.Column( db.String(200), nullable=False)
    hyperdrive_rating =db.Column( Float, nullable=False)
    MGLT =db.Column( db.Integer, nullable=False)
    url =db.Column( db.String(200), nullable=False)

    def __repr__(self):
        return '<id %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.height,
            "manufacturer": self.mass,
            "cost_in_credits": self.hair_color,
            "length": self.skin_color,
            "max_atmosphering_speed": self.eye_color,
            "crew": self.birth_year,
            "passengers": self.gender,
            "cargo_capacity": self.homeworld,
            "consumables":self.consumables,
            "hyperdrive_rating":self.hyperdrive_rating,
            "MGLT":self.mglt,
            "url": self.url
        }

class Species(db.Model):
    # __tablename__ = 'Species'
    id =db.Column( db.Integer, primary_key=True)
    name =db.Column( db.String(50), nullable=True)
    classification =db.Column( db.String(200), nullable=False)
    designation =db.Column( db.String(200), nullable=False)
    average_height =db.Column( db.Integer, nullable=False)
    skin_colors =db.Column( db.String(200), nullable=False)
    hair_colors =db.Column( db.String(200), nullable=False)
    eye_colors =db.Column( db.String(200), nullable=False)
    average_lifespan =db.Column( db.Integer, nullable=False)
    homeworld =db.Column( db.String(200), nullable=False)
    language =db.Column( db.String(200), nullable=False)
    url =db.Column( db.String(200), nullable=False)

    def __repr__(self):
        return '<id %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "classification": self.classification,
            "designation": self.designation,
            "average_height": self.average_height,
            "skin_colors": self.skin_colors,
            "hair_colors": self.hair_colors,
            "eye_colors": self.eye_colors,
            "average_lifespan": self.average_lifespan,
            "homeworld": self.homeworld,
            "language":self.language,
            "url": self.url
        }

class User(db.Model):
    # __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active
            # do not serialize the password, its a security breach
        }

class Favorites(db.Model):
    # __tablename__ = 'Favorites'
    favoriteid = db.Column( db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    tipo = db.Column( db.String(15), nullable=False)
    name = db.Column( db.String(50), nullable=True)


    
    def to_dict(self):
        return '<favoriteid %r>' % self.favoriteid
    
    def serialize(self):
        return {
            "favoriteid": self.favoriteid,
            "user_id": self.user_id,
            "type": self.type
        }