class Livro:
    def __init__(self, titulo: str, autor: str, categoria:str, paginas: int, isbn: str, preco: float):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.__paginas = paginas
        self.isbn = isbn
        self.__preco = preco
        self.id = None
    
    @property
    def paginas(self):
        return self.__paginas
    
    @property
    def preco(self):
        return self.__preco
    
    def __str__(self):
        return f"{self.titulo} - ${self.autor}"
    