from app import api, app, db
from flask_restx import Resource, marshal
from flask import jsonify
from app.parser import userRequestParser
from app.serializer import user_details
from app.models import User
from flask_jwt_extended import create_access_token

@app.route("/test")
def test():
    return "<h1> Flask Application Working Successfully. </h1>"

# FlaskRestx

@api.route('/user')
class UserViews(Resource):
    
    # POST method
    def post(self):
        req_body = userRequestParser.parse_args()

        if User.query.filter_by(name=req_body['name']).all():
            
            return jsonify(status = 401, message = "User is already Present.")
        
        user = User(
            name = req_body['name'],
            dob = req_body['dob']
        )

        db.session.add(user)
        db.session.commit()

        return jsonify( data = marshal(user, user_details), status =  201)

    # GET method
    def get(self):
        users = User.query.all()
        return jsonify(data = marshal(users, user_details), status = 200)

@api.route('/user/<int:id>')
class ParticularUser(Resource):

    # GET method
    def get(self, id):
        user = User.query.get(id)
        if user:
            return jsonify(data = marshal(user, user_details), status = 200)
        
        return jsonify(status = 401, message = "User Not Found!!")
    
    # DELETE method
    def delete(self, id):
        user = User.query.get(id)

        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify(status = 200, deleted_data = marshal(user, user_details))
        
        return jsonify(status = 401, message = "User Not Found!!")
    
@api.route('/user/login')
class Login(Resource):

    # POST method
    def post(self):
        req_body  = userRequestParser.parse_args()

        user = User.query.filter_by(
            name = req_body['name'],
            dob = req_body['dob']
        ).first()
        
        if user:
            access_token = create_access_token(identity=req_body['name'])
            return jsonify(access_token = access_token, status = 200)
        
        return jsonify(message = "'Name' or 'DOB' is incorrect.", status = 401)