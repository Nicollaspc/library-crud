from livro import Livro
from banco import BancoDeDados

def menu():
    print("[1] - Cadastrar Livro")
    print("[2] - Listar Livros")
    print("[3] - Atualizar Livros")
    print("[4] - Deletar livros")
    print("[5] - Sair")
    
bd = BancoDeDados()
bd.conectar()
bd.criar_tabela_livro()    

while True:
    
    menu()

    opcao = int(input("Opção: "))

    match opcao:
        case 1:
            titulo = input("Título: ")
            autor = input("Autor: ")
            paginas = int(input("Páginas: "))
            isbn = input("ISBN: ")
            preco = float(input("Preço: "))
            
            livro = Livro(titulo,autor,paginas,isbn,preco)
            bd.criar_livro(livro)
            print("Livro cadastrado com sucesso")
        
        case 2:    
            livros = bd.listar_livro()
            
            if livros: 
                for livro in livros:
                    print(livro.titulo)
        
        case 3:
            titulo_livro = input("Título: ")
            preco = float(input("Preço: "))
            
            bd.atualizar_preco_livro(preco,titulo_livro)

            print("Preço atualizado com sucesso")
        
        case 4:
            titulo = input("Título: ")
            
            bd.deletar_livro(titulo)

            print("Livro deletado com sucesso")
        
        case 5:
            bd.fechar_conexao()
            print("Sistema encerrado.")
            break
        
        case _:
            print("Opçao inválida")