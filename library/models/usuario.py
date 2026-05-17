class Usuario:
    def __init__(self,nome: str, email: str, senha: str) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha
    
    def __str__(self) -> None:
        print(f"Nome:{self.nome}")