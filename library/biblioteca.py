from livro import Livro
from exceptions.bibliotecaVazia import BibliotecaVaziaError

class Biblioteca:
    def __init__(self,banco) -> None:
        self.banco = banco
    
    def _validar_lista(self):
        if not self.banco.listar_livro():
            raise BibliotecaVaziaError("Nenhum livro cadastrado")
            
    def adicionar_livro(self, livro: Livro) -> None:
        self.banco.criar_livro(livro)
    
    def remover_livro(self, isbn: str) -> bool:
        self._validar_lista()
        
        livro = self.buscar_livro(isbn)

        if not livro:
            return False
        
        self.banco.deletar_livro(isbn)
        
        return True
    
    def listar_livros(self) -> list[Livro]:
        self._validar_lista()
        
        return self.banco.listar_livro().copy()
    
    def buscar_livro(self, isbn: str) -> Livro | None:
        self._validar_lista()
        
        livros = self.banco.listar_livro()
        
        for livro in livros:
            if livro.isbn == isbn:
                return livro
            
        return None
    
    def atualizar_preco(self,isbn,novo_preco) -> bool:
        livro = self.buscar_livro(isbn)
        
        if not livro:
            return False

        self.banco.atualizar_preco_livro(novo_preco,isbn)
        
        return True