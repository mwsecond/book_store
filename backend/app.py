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

    def to_dict(self):
        return {'id': self.id, 'nome': self.nome, 'email': self.email}


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
    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'genero': self.genero,
            'autor': self.autor,
            'preco': self.preco,
            'sinopse': self.sinopse,
            'foto': self.foto,
            'num_total': self.num_total,
            'admin_id': self.admin_id
        }


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

@app.route('/admins/<int:admin_id>', methods=['PUT'])
def update_admin(admin_id):
    # Encontra o admin pelo ID. Se não achar, retorna erro 404 (Not Found)
    admin = Admin.query.get_or_404(admin_id)
    
    # Pega os novos dados da requisição
    dados = request.get_json()
    
    # Atualiza os campos do objeto admin
    admin.nome = dados['nome']
    admin.email = dados['email']
    # (Não atualizamos a senha aqui por simplicidade, mas seria possível)
    
    # Salva as alterações no banco de dados
    db.session.commit()
    
    return jsonify({'message': 'Admin atualizado com sucesso!'})

@app.route('/admins/<int:admin_id>', methods=['DELETE'])
def delete_admin(admin_id):
    # Encontra o admin pelo ID. Se não achar, retorna erro 404 (Not Found)
    admin = Admin.query.get_or_404(admin_id)
    
    db.session.delete(admin)
    
    # Salva as alterações no banco de dados
    db.session.commit()
    
    return jsonify({'message': 'Admin deleteado com sucesso!'})

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    
    novo_usuario = Usuario(nome=dados['nome'], email=dados['email'], senha=dados['senha'])
    
    db.session.add(novo_usuario)
    db.session.commit()
    
    return jsonify({'message': 'usuario criado com sucesso!'}), 201

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    
    lista_usuarios = [usuario.to_dict() for usuario in usuarios]
    
    return jsonify(lista_usuarios)

@app.route('/usuarios/<int:usuario_id>', methods=['PUT'])
def update_usuario(usuario_id):
    # Encontra o usuario pelo ID. Se não achar, retorna erro 404 (Not Found)
    usuario = Usuario.query.get_or_404(usuario_id)
    
    # Pega os novos dados da requisição
    dados = request.get_json()
    
    # Atualiza os campos do objeto usuario
    usuario.nome = dados['nome']
    usuario.email = dados['email']
    # (Não atualizamos a senha aqui por simplicidade, mas seria possível)
    
    # Salva as alterações no banco de dados
    db.session.commit()
    
    return jsonify({'message': 'usuario atualizado com sucesso!'})

@app.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
def delete_usuario(usuario_id):
    # Encontra o usuario pelo ID. Se não achar, retorna erro 404 (Not Found)
    usuario = Usuario.query.get_or_404(usuario_id)
    
    db.session.delete(usuario)
    
    # Salva as alterações no banco de dados
    db.session.commit()
    
    return jsonify({'message': 'usuario deleteado com sucesso!'})

@app.route('/livros', methods=['POST'])
def criar_livro():
    dados = request.get_json()
    
    # Criamos o objeto com todos os dados do livro, incluindo a FK
    novo_livro = Livro(
        titulo=dados['titulo'],
        genero=dados['genero'],
        autor=dados['autor'],
        preco=dados['preco'],
        sinopse=dados['sinopse'],
        foto=dados.get('foto'), # .get() é mais seguro se o campo for opcional
        num_total=dados['num_total'],
        admin_id=dados['admin_id'] # Passamos o ID do admin que criou o livro
    )
    
    db.session.add(novo_livro)
    db.session.commit()
    
    return jsonify({'message': 'Livro criado com sucesso!'}), 201

# Rota para LER todos os Livros (GET)
@app.route('/livros', methods=['GET'])
def get_livros():
    livros = Livro.query.all()
    lista_livros = [livro.to_dict() for livro in livros]
    return jsonify(lista_livros)

@app.route('/livros/<int:livro_id>', methods=['PUT'])
def update_livro(livro_id):
    livro = Livro.query.get_or_404(livro_id)
    dados = request.get_json()
    
    livro.titulo = dados['titulo']
    livro.genero = dados['genero']
    livro.autor = dados['autor']
    livro.sinopse = dados['sinopse']
    livro.preco = dados['preco']
    livro.foto = dados.get('foto')
    livro.num_total = dados['num_total']
    # (Não atualizamos a senha aqui por simplicidade, mas seria possível)
    
    # Salva as alterações no banco de dados
    db.session.commit()
    
    return jsonify({'message': 'Livro atualizado com sucesso!'}), 201

@app.route('/livros/<int:livro_id>', methods=['DELETE'])
def delete_livro(livro_id):
    # Encontra o livro pelo ID. Se não achar, retorna erro 404 (Not Found)
    livro = Livro.query.get_or_404(livro_id)
    
    db.session.delete(livro)
    
    # Salva as alterações no banco de dados
    db.session.commit()
    
    return jsonify({'message': 'livro deleteado com sucesso!'})


if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)