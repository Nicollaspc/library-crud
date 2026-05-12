import sqlite3
from livro import Livro
class BancoDeDados:
    def __init__(self, nome_banco="library/database/banco.sqlite" ) -> None:
        self.nome_banco = nome_banco
        self.conn = None
    
    def conectar(self):
        try:    
            self.conn = sqlite3.connect(self.nome_banco)
            print("conectado")
        except sqlite3.DatabaseError as e:
            raise sqlite3.DatabaseError(f"Erro de conexão com o banco de dados: {e}")
    
    def criar_tabela_livro(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS livro(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    paginas INTEGER NOT NULL,
                    isbn TEXT NOT NULL,
                    preco FLOAT NOT NULL
                )""")
                self.conn.commit()
            except sqlite3.Error as e:
                raise sqlite3.Error(f"Erro ao criar tabela Livros: {e}")
    
    def criar_livro(self, livro: Livro):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """
                    INSERT INTO livro (titulo,autor,categoria,paginas,isbn,preco)
                    VALUES (?,?,?,?,?)
                    """,
                    (livro.titulo,livro.autor,livro.categoria,livro.paginas,livro.isbn,livro.preco)
                )
                self.conn.commit()
            except sqlite3.DataError as e:
                raise sqlite3.DataError(f"Dados incorretos: {e}")
        
    
    def listar_livro(self):
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
            
            except sqlite3.Error as e:
                raise sqlite3.Error(f"Erro ao listar livros: {e}")
    
    def atualizar_preco_livro(self, preco_livro: float, isbn: str):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    "UPDATE livro SET preco = ? WHERE isbn = ?",
                    (preco_livro, isbn)
                )
                self.conn.commit()
            except sqlite3.Error as e:
                raise sqlite3.Error(f"Erro ao dar update no preco do livro com o isbn {isbn}: {e}")
    
    def deletar_livro(self, titulo_livro):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    "DELETE FROM livro Where titulo = ?",
                    (titulo_livro,))
                self.conn.commit()
            except sqlite3.Error as e:
                raise sqlite3.Error(f"Erro ao deletar livro: {e}")
    
    def fechar_conexao(self):
        if self.conn:
            self.conn.close()
            self.conn = None

