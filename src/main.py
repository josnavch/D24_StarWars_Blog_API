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

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/planets', methods=['GET'])
def handle_get_planets():

    query = Planets.query.all()

    # map the results and your list of planets  inside of the all_planets variable
    all_planets = list(map(lambda x: x.serialize(), query))

    return jsonify(all_planets), 200

@app.route('/addplanets', methods=['POST'])
def handle_add_planets():
   
    request_body = request.get_json()
    #task = Todo(label=str("Ir a la pulpe"), done=False)
    planet = Planets(
        name = request_body["name"], 
        rotation_period = request_body["rotation_period"],
        orbital_period = request_body["orbital_period"],
        diameter = request_body["diameter"],
        climate = request_body["climate"],
        gravity = request_body["gravity"],
        terrain = request_body["terrain"],
        surface_water = request_body["surface_water"],
        population = request_body["population"],
        url = request_body["url"]
        )
    db.session.add(planet)
    db.session.commit()

    return jsonify("Planet added correctly."), 200
    


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
