from flask import request, jsonify, Blueprint
from . import db
from .models import Admin, Usuario, Livro, Avaliacao
from .schemas import admin_schema, admins_schema, usuario_schema, usuarios_schema
from marshmallow import ValidationError

main = Blueprint('main', __name__)

@main.route("/")
def read_root():
    return jsonify({"message": "API Flask com Modelo Admin definido!"})
@main.route('/admins', methods=['POST'])
def criar_admin():
    json_data = request.get_json()
    try:
        # O schema carrega e valida os dados recebidos
        novo_admin = admin_schema.load(json_data)
    except ValidationError as err:
        # Se a validação falhar, retorna um erro 400 com as mensagens
        return jsonify(err.messages), 400

    # Adiciona o novo objeto validado ao banco
    db.session.add(novo_admin)
    db.session.commit()

    # Retorna uma mensagem e o objeto que foi criado
    return jsonify({
        "message": "Admin criado com sucesso!",
        "admin": admin_schema.dump(novo_admin)
    }), 201

@main.route('/admins', methods=['GET'])
def get_admins():
    admins = Admin.query.all()
    # O schema cuida de toda a conversão para JSON!
    return admins_schema.dump(admins)

@main.route('/admins/<int:admin_id>', methods=['PUT'])
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

@main.route('/admins/<int:admin_id>', methods=['DELETE'])
def delete_admin(admin_id):
    # Encontra o admin pelo ID. Se não achar, retorna erro 404 (Not Found)
    admin = Admin.query.get_or_404(admin_id)
    
    db.session.delete(admin)
    
    # Salva as alterações no banco de dados
    db.session.commit()
    
    return jsonify({'message': 'Admin deleteado com sucesso!'})

@main.route('/usuarios', methods=['POST'])
def criar_usuario():
    json_data = request.get_json()
    try:
        # O schema carrega e valida os dados recebidos
        novo_usuario = usuario_schema.load(json_data)
    except ValidationError as err:
        # Se a validação falhar, retorna um erro 400 com as mensagens
        return jsonify(err.messages), 400

    # Adiciona o novo objeto validado ao banco
    db.session.add(novo_usuario)
    db.session.commit()

    # Retorna uma mensagem e o objeto que foi criado
    return jsonify({
        "message": "Usuario criado com sucesso!",
        "usuario": usuario_schema.dump(novo_usuario)
    }), 201
@main.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    # O schema cuida de toda a conversão para JSON!
    return usuarios_schema.dump(usuarios)

@main.route('/usuarios/<int:usuario_id>', methods=['PUT'])
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

@main.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
def delete_usuario(usuario_id):
    # Encontra o usuario pelo ID. Se não achar, retorna erro 404 (Not Found)
    usuario = Usuario.query.get_or_404(usuario_id)
    
    db.session.delete(usuario)
    
    # Salva as alterações no banco de dados
    db.session.commit()
    
    return jsonify({'message': 'usuario deleteado com sucesso!'})

@main.route('/livros', methods=['POST'])
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
@main.route('/livros', methods=['GET'])
def get_livros():
    livros = Livro.query.all()
    lista_livros = [livro.to_dict() for livro in livros]
    return jsonify(lista_livros)

@main.route('/livros/<int:livro_id>', methods=['PUT'])
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
    
    # Salva as alterações no banco de dados
    db.session.commit()
    
    return jsonify({'message': 'Livro atualizado com sucesso!'}), 200

@main.route('/livros/<int:livro_id>', methods=['DELETE'])
def delete_livro(livro_id):
    # Encontra o livro pelo ID. Se não achar, retorna erro 404 (Not Found)
    livro = Livro.query.get_or_404(livro_id)
    
    db.session.delete(livro)
    
    # Salva as alterações no banco de dados
    db.session.commit()
    
    return jsonify({'message': 'livro deleteado com sucesso!'})

@main.route('/avaliacoes', methods=['POST'])
def criar_avaliacao():
    dados = request.get_json()
    
    # Criamos o objeto com todos os dados do avaliacao, incluindo a FK
    novo_avaliacao = Avaliacao(
        comentario=dados['comentario'],
        estrelas=dados['estrelas'],
        livro_id=dados['livro_id'],
        usuario_id=dados['usuario_id']
    )
    
    db.session.add(novo_avaliacao)
    db.session.commit()
    
    return jsonify({'message': 'avaliacao criado com sucesso!'}), 201

# Rota para LER todos os avaliacoes (GET)
@main.route('/avaliacoes', methods=['GET'])
def get_avaliacoes():
    avaliacoes = Avaliacao.query.all()
    lista_avaliacoes = [avaliacao.to_dict() for avaliacao in avaliacoes]
    return jsonify(lista_avaliacoes)

@main.route('/avaliacoes/<int:avaliacao_id>', methods=['PUT'])
def update_avaliacao(avaliacao_id):
    # Encontra o avaliacao pelo ID. Se não achar, retorna erro 404 (Not Found)
    avaliacao = Avaliacao.query.get_or_404(avaliacao_id)
    
    # Pega os novos dados da requisição
    dados = request.get_json()
    
    # Atualiza os campos do objeto avaliacao
    avaliacao.comentario = dados['comentario']
    avaliacao.estrelas = dados['estrelas']
    
    db.session.commit()
    
    return jsonify({'message': 'avaliacao atualizado com sucesso!'})

@main.route('/avaliacoes/<int:avaliacao_id>', methods=['DELETE'])
def delete_avaliacao(avaliacao_id):
    # Encontra o avaliacao pelo ID. Se não achar, retorna erro 404 (Not Found)
    avaliacao = Avaliacao.query.get_or_404(avaliacao_id)
    
    db.session.delete(avaliacao)
    
    # Salva as alterações no banco de dados
    db.session.commit()

    return jsonify({'message': 'Avaliação deletada com sucesso!'})