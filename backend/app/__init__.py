# app/__init__.py
from flask_cors import CORS
from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

    # --- Configuração do Banco de Dados ---
    # (sua configuração continua a mesma)
    USER = 'root'
    PASSWORD = '131412' 
    HOST = 'localhost'
    DATABASE = 'book_store'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config["JWT_SECRET_KEY"] = "bookstoreisverycool"

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

    # Importa o Blueprint do arquivo de rotas
    from .routes import main as main_blueprint
    # Registra o Blueprint na aplicação
    app.register_blueprint(main_blueprint)

    with app.app_context():
        from . import models
        db.create_all()

    return app