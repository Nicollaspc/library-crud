from repository.livro_repository import LivroRepository
from models.livro import Livro
from exceptions.bibliotecaVazia import BibliotecaVaziaError

class LivroService:
    def __init__(self) -> None:
        self.repository = LivroRepository()
        
    
    def _validar_livro(self):
        livros = self.repository.listar_livro()
        
        if not livros:
            raise BibliotecaVaziaError("")
        
        return livros
    
    def adicionar_livro(self, livro: Livro):
        self.repository.criar_livro(livro)
    
    def listar_livro(self):
        livros = self._validar_livro()
        return livros
    
    def buscar_livro(self, isbn: str) -> Livro | None:
        livros = self._validar_livro()
        
        for livro in livros:
            if livro.isbn == isbn:
                return livro
    
    def remover_livro(self,isbn) -> bool:
        livro = self.buscar_livro(isbn)
        
        if not livro:
            return False
        
        self.repository.deletar_livro(isbn)
        return True
    
    def atualizar_preco(self, isbn: str, preco: float) -> bool:
        livro = self.buscar_livro(isbn)
        
        if not livro:
            return False
        
        self.repository.atualizar_preco_livro(preco,isbn)
        return True