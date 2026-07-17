from repositories.users import get_one_user, add_users , get_users
from flask_jwt_extended import create_access_token
import bcrypt
class AuthServices():
    def hash_password(self , password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt).decode("utf-8")
    def register(self , data):
        username = data.get("username")
        password = data.get("password")
        if not username or not password:
            return {"message":"missing fields"},400
        user = get_users(username)
        if user is not None:
            return {"message":"username already exists"},409
        hashed_password = self.hash_password(password)
        add_users(username , hashed_password)
        return{"message":"registration sucessfull"},201
    def login(self, data):
        username = data.get("username")
        password = data.get("password")

        user = get_one_user(username)

        stored_password = user[0]

        if not bcrypt.checkpw(password.encode(), stored_password.encode()):
           return {"message": "invalid password"}, 400

        token = create_access_token(identity=username)
        return {"access_token": token}
        
        