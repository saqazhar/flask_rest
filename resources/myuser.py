from flask_restful import Resource, reqparse
from models.myuser import User


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type= str,
        required = True,
        help = "This field cannot be empty."
    )
    parser.add_argument('password',
        type= str,
        required = True,
        help = "This field cannot be empty."
    )
    def post(self):
        data = UserRegister.parser.parse_args()
        if User.find_by_username(data['username']):
            return {"Mesaage":"User Already Exist"}
        
        user = User(data['username'], data['password'])
        user.save_to_db()
        return {"message": "user created succesfully"}

