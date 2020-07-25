"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db, Homeless_User, Shelter, Contributor, Deposit 
from admin import setup_admin
from flask_jwt_simple import (
    JWTManager, jwt_required, create_jwt, get_jwt_identity
)


#from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False

# Setup the Flask-JWT-Simple extension
app.config['JWT_SECRET_KEY'] =  os.environ.get('FLASK_APP_KEY')
jwt = JWTManager(app)

app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')

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


@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    params = request.get_json()
    username = params.get('email', None)
    password = params.get('password', None)

    if not username:
        return jsonify({"msg": "Missing email parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    user = Homeless_User.query.filter_by(email=username,password=password).first() 

    if user is None:
        return jsonify({"msg": "Bad username or password"}), 401



    # Identity can be any data that is json serializable
    ret = {'jwt': create_jwt(identity=user.id), "user_id": user.id}
    return jsonify(ret), 200



@app.route('/futurehomeowner', methods=['POST', 'GET'])
def who_is_homeless():

    # POST request
    if request.method == 'POST':
        body = request.get_json()

        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)
        if 'username' not in body:
            raise APIException('You need to specify the username', status_code=400)
        if 'email' not in body:
            raise APIException('You need to specify the email', status_code=400)
        existing_user = Homeless_User.query.filter_by(email=body["email"]).first()
        if existing_user is not None:
            raise APIException('Please check your email is correct', status_code=400)
        if 'password' not in body:
            raise APIException('You need to specify the password', status_code=400)
        if 'currently_homless' not in body:
            raise APIException('You need to specify if you are homeless or not', status_code=400)
        story = ''
        if "story" in body:
            story = body['story']
        homeless_person = Homeless_User(username=body['username'], 
        email=body['email'], 
        password=body['password'],currently_homless=body['currently_homless'],
        story=story,
        phone_number=body['phone_number']) 


        db.session.add(homeless_person)
        db.session.commit()
        return "ok", 200
    
    # GET request
    if request.method == 'GET':
        Homeless_Users = Homeless_User.query.all()
        Homeless_Users = list(map(lambda x: x.serialize(), Homeless_Users))
        return jsonify(Homeless_Users), 200

    return "Invalid Method", 404



################ 
# Single person
################


@app.route('/futurehomeowner/<int:homeless_user_id>', methods=['PUT', 'GET', 'DELETE'])
def get_homeless_person(homeless_user_id):
# PUT request
    if request.method == 'PUT':
        body = request.get_json()
        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)
        user1 = Homeless_User.query.get(homeless_user_id)
        if user1 is None:
            raise APIException('User not found', status_code=404)
        if "username" in body:
            user1.username = body["username"]
        # if "email" in body:
        #     user1.email = body["email"]
        db.session.commit()
        return jsonify(user1.serialize()), 200
# GET request
    if request.method == 'GET':
        user1 = Homeless_User.query.get(homeless_user_id)
        if user1 is None:
            raise APIException('User not found', status_code=404)
        return jsonify(user1.serialize()), 200
    # DELETE request
    if request.method == 'DELETE':
        user1 = Homeless_User.query.get(homeless_user_id)
        if user1 is None:
            raise APIException('User not found', status_code=404)
        db.session.delete(user1)
        db.session.commit()
        return "ok", 200
    return "Invalid Method", 404



#     # PUT request
#     if request.method == 'PUT':
#         body = request.get_json()
#         if body is None:
#             raise APIException("You need to specify the request body as a json object", status_code=400)
#         user1 = Person.query.get(person_id)
#         if user1 is None:
#             raise APIException('User not found', status_code=404)
#         if "username" in body:
#             user1.username = body["username"]
#         if "email" in body:
#             user1.email = body["email"]
#         if "story" in body:
#             user1.username = body["story"]
#         db.session.commit()

#         return jsonify(user1.serialize()), 200




@app.route('/shelter', methods=['POST', 'GET'])
def i_am_a_shelter():

    # POST request
    if request.method == 'POST':
        body = request.get_json()

        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)
        if 'shelter_name' not in body:
            raise APIException('You need to specify the name of your shelter.', status_code=400)
        if 'address_1' and 'address_2'not in body:
            raise APIException('You need to specify the address.', status_code=400)
        
        shelter_object = Shelter(shelter_name=body['shelter_name'], shelter_to_homeless_user=body["shelter_to_homeless_user"], address_1=body['address_1'], address_2=body['address_2'])
        db.session.add(shelter_object)
        db.session.commit()
        return "ok", 200
    
    # GET request
    if request.method == 'GET':
        all_shelters = Shelter.query.all()
        all_shelters = list(map(lambda x: x.serialize(), all_shelters))
        return jsonify(all_shelters), 200

    return "Invalid Method", 404


@app.route('/heroes', methods=['POST', 'GET'])
def i_am_a_hero():

    # POST request
    if request.method == 'POST':
        body = request.get_json()

        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)
        if 'username' not in body:
            raise APIException('You need to specify the username', status_code=400)
        if 'email' not in body:
            raise APIException('You need to specify the email', status_code=400)
        if 'password' not in body:
            raise APIException('You need to specify the password', status_code=400)

        heroes = Contributor(
            username = body['username'], 
            email = body['email'], 
            password = body['password'],
            # number_of_contributions = body['number_of_contributions']
            )

        db.session.add(heroes)
        db.session.commit()
        return "ok", 200
    
    # GET request
    if request.method == 'GET':
        all_contributors = Contributor.query.all()
        all_contributors = list(map(lambda x: x.serialize(), all_contributors))
        return jsonify(all_contributors), 200

    return "Invalid Method", 404






@app.route('/donation', methods=['POST', 'GET'])
def i_am_helping_someone():

    # POST request
    if request.method == 'POST':
        body = request.get_json()

        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)
        if 'homeless_user_id' not in body:
            raise APIException('You need to select someone to donate to.', status_code=400)
        if 'contributor_user_id' not in body:
            raise APIException('Error, please report this as a bug.', status_code=400)
        
        donation_for_future_homeowner = Deposit(
            homeless_user_id=body['homeless_user_id'], 
            # shelter_to_homeless_user=body["shelter_to_homeless_user"], 
            contributor_user_id=body['contributor_user_id'], amount=body['amount']
            )
        db.session.add(donation_for_future_homeowner)
        db.session.commit()
        return "ok", 200

    
    # GET request
    if request.method == 'GET':
        all_deposits = Deposit.query.all()
        all_deposits = list(map(lambda x: x.serialize(), all_deposits))
        return jsonify(all_deposits), 200

    return "Invalid Method", 404



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)