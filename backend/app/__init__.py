# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)

    # --- Configuração do Banco de Dados ---
    # (sua configuração continua a mesma)
    USER = 'root'
    PASSWORD = '1235' 
    HOST = 'localhost'
    DATABASE = 'book_store'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)

    # Importa o Blueprint do arquivo de rotas
    from .routes import main as main_blueprint
    # Registra o Blueprint na aplicação
    app.register_blueprint(main_blueprint)

    with app.app_context():
        from . import models
        db.create_all()

    return app