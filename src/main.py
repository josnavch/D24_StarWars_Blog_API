"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planets, People, Starships, Species, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)
    
# ***************************** BEGIN USERS ***************************** 
@app.route('/user', methods=['GET'])
def handle_get_users():

    query = User.query.all()
    if not query:
        raise APIException('Users not found', status_code=404)
    else:
        all_users = list(map(lambda x: x.serialize(), query))

    return jsonify(all_users), 200

@app.route('/user/<int:user_id>', methods=['GET'])
def handle_get_user(user_id):

    query = User.query.get(user_id)

    if not query:
        raise APIException('User not found', status_code=404)
    else:
        user = query.serialize()

    return jsonify(user), 200
# ***************************** END USERS ***************************** 

# ***************************** BEGIN USERS FAVORITES ***************************** 
@app.route('/user/<int:user_id>/favorites', methods=['GET'])
def handle_get_user_favorites(user_id):

    query = Favorites.query.filter_by(user_id=user_id)

    if not query:
        raise APIException('User favorites not found', status_code=404)
    else:
        favorites = list(map(lambda x: x.serialize(), query))

    return jsonify(favorites), 200

@app.route('/user/<int:user_id>/favorites', methods=['POST'])
def handle_add_user_favorite(user_id):
    
    request_body = request.get_json()
    user = Favorites(
        user_id = user_id, 
        tipo = request_body["tipo"],
        name = request_body["name"]
        )
    db.session.add(user)
    db.session.commit()

    return jsonify("Favorite added correctly."), 200

@app.route('/favorite/<int:favorite_id>', methods=['DELETE'])
def handle_delete_favorite(favorite_id):

    favorite = Favorites.query.get(favorite_id)
   
    if favorite is None:
        raise APIException('Favorite not found', status_code=404)
    db.session.delete(favorite)
    db.session.commit()

    return jsonify("Favorite successfully removed.",favorite.name), 200
# ***************************** END USERS FAVORITES ***************************** 

# ***************************** BEGIN PLANETS ***************************** 
@app.route('/planets', methods=['GET'])
def handle_get_planets():

    query = Planets.query.all()

    # map the results and your list of planets  inside of the all_planets variable
    all_planets = list(map(lambda x: x.serialize(), query))

    return jsonify(all_planets), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def handle_get_planet_detail(planet_id):
    
    query = Planets.query.get(planet_id)

    if not query:
        raise APIException('Planet not found', status_code=404)
    else:
        planet = query.serialize()

    return jsonify(planet), 200

@app.route('/addplanets', methods=['POST'])
def handle_add_planets():
   
    request_body = request.get_json()

    # planet = Planets(
    #     name = request_body["name"], 
    #     rotation_period = request_body["rotation_period"],
    #     orbital_period = request_body["orbital_period"],
    #     diameter = request_body["diameter"],
    #     climate = request_body["climate"],
    #     gravity = request_body["gravity"],
    #     terrain = request_body["terrain"],
    #     surface_water = request_body["surface_water"],
    #     population = request_body["population"],
    #     url = request_body["url"]
    #     )
    #db.session.add_all(planet)
    db.session.bulk_insert_mappings(Planets, request_body)
    db.session.commit()

    return jsonify("Planet added correctly."), 200

@app.route('/planets/<int:planet_id>', methods=['DELETE'])
def handle_delete_planet(planet_id):

    planet = Planets.query.get(planet_id)
   
    if planet is None:
        raise APIException('Planet not found', status_code=404)
    db.session.delete(planet)
    db.session.commit()

    return jsonify("Planet successfully removed.",planet.name), 200
    
# ***************************** END PLANETS ***************************** 

# ***************************** BEGIN PEOPLE ***************************** 
@app.route('/people', methods=['GET'])
def handle_get_people():

    query = People.query.all()

    # map the results and your list of planets  inside of the all_planets variable
    all_people = list(map(lambda x: x.serialize(), query))

    return jsonify(all_people), 200

@app.route('/people/<int:people_id>', methods=['GET'])
def handle_get_people_detail(people_id):
    
    query = People.query.get(people_id)

    if not query:
        raise APIException('People not found', status_code=404)
    else:
        people = query.serialize()

    return jsonify(people), 200

@app.route('/addpeople', methods=['POST'])
def handle_add_people():
   
    request_body = request.get_json()

    db.session.bulk_insert_mappings(People, request_body)
    db.session.commit()

    return jsonify("People added correctly."), 200

@app.route('/people/<int:people_id>', methods=['DELETE'])
def handle_delete_people(people_id):

    people = People.query.get(people_id)
   
    if people is None:
        raise APIException('People not found', status_code=404)
    db.session.delete(people)
    db.session.commit()

    return jsonify("People successfully removed.",people.name), 200

# ***************************** END PEOPLE ***************************** 

# ***************************** BEGIN STARSHIPS ***************************** 
@app.route('/starships', methods=['GET'])
def handle_get_starships():

    query = Starships.query.all()

    if not query:
        raise APIException('Starships not found', status_code=404)
    else:
        all_starships = list(map(lambda x: x.serialize(), query))

    return jsonify(all_starships), 200

@app.route('/starships/<int:starship_id>', methods=['GET'])
def handle_get_starship_detail(starship_id):
    
    query = Starships.query.get(starship_id)

    if not query:
        raise APIException('Starship not found', status_code=404)
    else:
        starship = query.serialize()

    return jsonify(starship), 200

@app.route('/addstarships', methods=['POST'])
def handle_add_starships():
   
    request_body = request.get_json()

    db.session.bulk_insert_mappings(Starships, request_body)
    db.session.commit()

    return jsonify("Starships added correctly."), 200

@app.route('/starships/<int:starship_id>', methods=['DELETE'])
def handle_delete_starship(starship_id):

    starship = Starships.query.get(starship_id)
   
    if starship is None:
        raise APIException('Starship not found', status_code=404)
    db.session.delete(starship)
    db.session.commit()

    return jsonify("Starship successfully removed.",starship.name), 200
# ***************************** END STARSHIPS *****************************

# ***************************** BEGIN SPECIES ***************************** 
@app.route('/species', methods=['GET'])
def handle_get_species():

    query = Species.query.all()

    if not query:
        raise APIException('Species not found', status_code=404)
    else:
        all_species = list(map(lambda x: x.serialize(), query))

    return jsonify(all_species), 200

@app.route('/species/<int:species_id>', methods=['GET'])
def handle_get_species_detail(species_id):
    
    query = Species.query.get(species_id)

    if not query:
        raise APIException('Species not found', status_code=404)
    else:
        species = query.serialize()

    return jsonify(species), 200

@app.route('/addspecies', methods=['POST'])
def handle_add_species():
   
    request_body = request.get_json()

    db.session.bulk_insert_mappings(Species, request_body)
    db.session.commit()

    return jsonify("Species added correctly."), 200

@app.route('/species/<int:species_id>', methods=['DELETE'])
def handle_delete_species(species_id):

    species = Species.query.get(species_id)
   
    if species is None:
        raise APIException('Species not found', status_code=404)
    db.session.delete(species)
    db.session.commit()

    return jsonify("Species successfully removed.",species.name), 200
# ***************************** END SPECIES *****************************

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
