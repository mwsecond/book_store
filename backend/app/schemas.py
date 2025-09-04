# app/schemas.py

from . import ma
from .models import Admin, Usuario

# Define o esquema de validação e serialização para o modelo Admin
class AdminSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Admin   # O modelo SQLAlchemy que este esquema representa
        load_instance = True  # Opcional: desserializa para um objeto do modelo
        include_fk = True # Opcional: inclui chaves estrangeiras na serialização

# Instancia os esquemas para uso
admin_schema = AdminSchema() # Para um único admin
admins_schema = AdminSchema(many=True) # Para uma lista de admins

# Define o esquema de validação e serialização para o modelo Admin
class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario   # O modelo SQLAlchemy que este esquema representa
        load_instance = True  # Opcional: desserializa para um objeto do modelo
        include_fk = True # Opcional: inclui chaves estrangeiras na serialização

# Instancia os esquemas para uso
usuario_schema = UsuarioSchema() # Para um único Usuario
usuarios_schema = UsuarioSchema(many=True) # Para uma lista de Usuarios