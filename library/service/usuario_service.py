from repository.usuario_repository import UsuarioRepository
from models.usuario import Usuario

class UsuarioService:
    def __init__(self) -> None:
        self.repositorio_usuario = UsuarioRepository()
    
    def adicionar_usuario(self, usuario: Usuario) -> None:
        self.repositorio_usuario.criar_usuario(usuario)
        
    
    def listar_usuario(self):
        pass
        
    
    def buscar_usuario(self, id: int) -> Usuario | None:
        pass
    
    def remover_usuario(self, id: int) -> Usuario | None: 
        pass