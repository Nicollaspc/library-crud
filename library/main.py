from livro import Livro
from banco import BancoDeDados
from biblioteca import Biblioteca
from exceptions.bibliotecaVazia import BibliotecaVaziaError

if __name__ == "__main__":

    def menu():
        print("[1] - Cadastrar Livro")
        print("[2] - Listar Livros")
        print("[3] - Atualizar Livros")
        print("[4] - Deletar livros")
        print("[5] - Buscar livro")
        print("[6] - Sair")
    
    bd = BancoDeDados()
    bd.conectar()
    bd.criar_tabela_livro()    

    biblioteca = Biblioteca(bd)

    while True:
    
        menu()

        try:
            opcao = int(input("Opção: "))

            match opcao:
                case 1:
                    titulo = input("Título: ")
                    autor = input("Autor: ")
                    paginas = int(input("Páginas: "))
                    isbn = input("ISBN: ")
                    preco = float(input("Preço: "))
                    
                    livro = Livro(titulo,autor,paginas,isbn,preco)
                    biblioteca.adicionar_livro(livro)
                    print("Livro cadastrado com sucesso")
                
                case 2:    
                    livros = biblioteca.listar_livros()
                    
                    if livros: 
                        for livro in livros:
                            print(f"Titulo: {livro.titulo}\nAutor: {livro.autor}\nPáginas: {livro.paginas}\nISBN: {livro.isbn}\nPreço: {livro.preco:.2f}")
                
                case 3:
                    isbn = input("ISBN: ")
                    preco = float(input("Preço: "))
                    
                    biblioteca.atualizar_preco(preco,isbn)

                    print("Preço atualizado com sucesso")
                
                case 4:
                    isbn = input("ISBN do livro: ")
                    
                    biblioteca.remover_livro(isbn)

                    print("Livro deletado com sucesso")
                
                case 5:
                    isbn = input("ISBN do livro: ")
                    
                    livro = biblioteca.buscar_livro(isbn)

                    if livro:
                        print(f"Titulo: {livro.titulo}\nAutor: {livro.autor}\nPáginas: {livro.paginas}\nISBN: {livro.isbn}\nPreço: {livro.preco:.2f}")
                    else:
                        print("Livro não encontrado")
                        
                case 6:
                    bd.fechar_conexao()
                    print("Sistema encerrado.")
                    break
                
                case _:
                    print("Opçao inválida")
                    
        except ValueError as e:
            print(f"Valor invalido: {e}")
        
        except BibliotecaVaziaError as e:
            print(e)
        
        except Exception as e:
            print(f"Erro inesperado: {e}")