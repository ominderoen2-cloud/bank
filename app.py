from repositories.fixed_account import create_fixed_account_table
from repositories.premium_account import create_premium_account_table
from repositories.junior_account import create_junior_account_table
from repositories.transactions import create_transactions_table
from repositories.users import create_users_table
from flask import Flask 
from flask_jwt_extended import JWTManager
from routes.auth_routes import auth_bp
import os
from routes.fixed_account_routes import fixed_bp
from routes.premium_account_routes import premium_bp
from routes.transactions_routes import trans_bp
from routes.junior_account_routes import junior_bp
app = Flask(__name__)
app.register_blueprint(fixed_bp)
app.register_blueprint(trans_bp)
app.register_blueprint(junior_bp)
app.register_blueprint(premium_bp)

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "dev-secret-change-me")
jwt = JWTManager(app)
app.register_blueprint(auth_bp)
@app.route("/")
def home():
    return{"status":"api running"}
create_fixed_account_table()
create_premium_account_table()
create_junior_account_table()
create_transactions_table()
create_users_table()
port = int(os.getenv("PORT", 5000))
if "__main__" == __name__:
    app.run(host = "0.0.0.0" , port = port , debug = False)
