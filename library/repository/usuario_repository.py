from models.usuario import Usuario
from database.connection import conectar
from psycopg2 import Error

class UsuarioRepository:
    def __init__(self) -> None:
        self.conn = conectar()
        
    def criar_usuario(self, usuario: Usuario):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("""INSERT INTO usuarios(
                    nome,
                    email,
                    senha
                    )
                    VALUES(%s, %s, %s)
                    """,(usuario.nome,usuario.email,usuario.senha))
                self.conn.commit()
                cursor.close()
            except Error as e:
                raise Error(f"Erro ao criar usuario: {e}")
    
    def listar_usuario(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM usuarios")
                resultado = cursor.fetchall()
                
                usuarios_list = []
                
                for linha in resultado:
                    usuario = Usuario(
                        nome=linha[1],
                        email=linha[2],
                        senha=linha[3]
                    )
                    usuarios_list.append(usuario)
                    
                cursor.close()
                return usuarios_list
            except Error as e:
                raise Error(f"Erro ao listar usuarios: {e}")
                
    def atualizar_usuario(self,nome: str, id:int):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("""UPDATE usuarios 
                            SET nome = %s
                            WHERE id = %s""",(nome,id))
                self.conn.commit()
                cursor.close()
            except Error as e:
                raise Error(f"Erro ao atualizar nome: {e}")
    
    def deletar_usuario(self,id:int):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("DELETE FROM usuarios WHERE id = %s",(id,))
                self.conn.commit()
                cursor.close()
            except Error as e:
                raise Error(f"Erro ao deletar usuario: {e}")
            
    
    def fechar_conexao(self):
        if self.conn:
            self.conn.close()
            self.conn = None
    