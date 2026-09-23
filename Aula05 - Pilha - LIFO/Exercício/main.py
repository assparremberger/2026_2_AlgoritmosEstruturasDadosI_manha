#Exercício:
# Construa um aplicativo para uma pilha de livros
# em que o livro possui título, autor e quantidade de páginas
# Devem ser construídos os seguintes métodos:
# 1) Adicionar livro na pilha
# 2) Remover um livro da pilha
# 3) Imprimir a pilha de livros
# 4) Retornar a posição de um livro na pilha, informando o título
# 5) Retornar os livros que estão na pilha, mas de um autor que o usuário informar
# 0) Sair
# Construa um menu de opções com as opções acima citadas
# O aplicativo só termina quando o usuário escolher a opção 0


from Pilha import Pilha
from Livro import Livro

lifo = Pilha()
def menu():
    print(f"""
    1. Adicionar Livros na pilha
    2. Remover um livro da pilha
    3. Imprimir a pilha de livros
    4. Buscar livro
    5. Buscar livro de autor
    0. Sair
""")
    return int( input("Digite sua opção: "))

op = -1

while op != 0:
    op = menu()
    if op == 1:
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o nome do autor: ")
        paginas = int( input("Digite a quantidade de páginas: ") )

        novo_livro = Livro(titulo, autor, paginas)
        lifo.add(novo_livro)
    elif op == 2:
        lifo.remover()
            
    elif op == 3:
        lifo.imprimir()
                
    elif op == 4:
        titulo_busca = input("Digite o nome do livro: ")
        lifo.getPosicao(titulo_busca)

    elif op == 5:
        buscar_autor = input("Digite o nome do autor: ")
        lifo.buscar_autor(buscar_autor)

    elif op == 0:
        print("Bye-Bye")

    else:
        print("Opção inválida, tente novamente.")
