from database.connection import conectar
from models.livro import Livro
from psycopg2 import Error

class LivroRepository:        
    def __init__(self) -> None:
        self.conn = conectar()
        
    def criar_livro(self, livro: Livro):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """
                    INSERT INTO livro (titulo,autor,categoria,paginas,isbn,preco)
                    VALUES (%s,%s,%s,%s,%s,%s)
                    """,
                    (livro.titulo,livro.autor,livro.categoria,livro.paginas,livro.isbn,livro.preco)
                )
                self.conn.commit()
                cursor.close()
                self.conn.close()
            except Error as e:
                raise Error(f"Erro ao criar livro: {e}")
        
    
    def listar_livro(self) -> list[Livro]:
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    "SELECT * FROM livro"
                )
                
                resultado = cursor.fetchall()
                
                livros = []
                
                for linha in resultado:
                    livro = Livro(titulo=linha[1],autor=linha[2],categoria=linha[3],paginas=linha[4],isbn=linha[5],preco=linha[6])
                    livros.append(livro)
                
                return livros
            
            except Error as e:
                raise Error(f"Erro ao listar livros: {e}")
        return []
    
    def atualizar_preco_livro(self, preco_livro: float, isbn: str):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    "UPDATE livro SET preco = %s WHERE isbn = %s",
                    (preco_livro, isbn)
                )
                self.conn.commit()
                cursor.close()
            except Error as e:
                raise Error(f"Erro ao dar update no preco do livro com o isbn {isbn}: {e}")
    
    def deletar_livro(self, titulo_livro):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    "DELETE FROM livro Where titulo = %s",
                    (titulo_livro,))
                self.conn.commit()
                cursor.close()
            except Error as e:
                raise Error(f"Erro ao deletar livro: {e}")
    

