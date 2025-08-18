from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


USER = 'root'
PASSWORD = '1235' 
HOST = 'localhost'
DATABASE = 'book_store'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 


db = SQLAlchemy(app)


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    
    
    def to_dict(self):
        return {'id': self.id, 'nome': self.nome, 'email': self.email}


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)


class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    genero = db.Column(db.String(100))
    autor = db.Column(db.String(255))
    preco = db.Column(db.Float)
    sinopse = db.Column(db.Text)
    foto = db.Column(db.String(255)) 
    num_total = db.Column(db.Integer)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)


class Avaliacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comentario = db.Column(db.Text)
    estrelas = db.Column(db.Integer)
    data = db.Column(db.DateTime, default=db.func.current_timestamp())
    livro_id = db.Column(db.Integer, db.ForeignKey('livro.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)



@app.route("/")
def read_root():
    return jsonify({"message": "API Flask com Modelo Admin definido!"})
@app.route('/admins', methods=['POST'])
def criar_admin():
    dados = request.get_json()
    
    novo_admin = Admin(nome=dados['nome'], email=dados['email'], senha=dados['senha'])
    
    db.session.add(novo_admin)
    db.session.commit()
    
    return jsonify({'message': 'Admin criado com sucesso!'}), 201

@app.route('/admins', methods=['GET'])
def get_admins():
    admins = Admin.query.all()
    
    lista_admins = [admin.to_dict() for admin in admins]
    
    return jsonify(lista_admins)


if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)