from Pilha import Pilha
lifo = Pilha()
def menu():
    print( " -------------------------------- ")
    print( "| 1) Adicionar na pila           |")
    print( "| 2) Remover da Pilha            |")
    print( "| 3) Imprimir Pilha              |")
    print( "| 4) Consultar posição na Pilha  |")
    print( "| 0) Sair                        |")
    print( " -------------------------------- ")
    return int( input( "Digite a opção desejada: ") )

op = -1
while op != 0:
    op = menu()
    if op == 1:
        lifo.add(  input("Digite o que será adicionado na pilha: ")  )
    elif op == 2:
        lifo.remove()
    elif op == 3: 
        lifo.imprimir()
    elif op == 4:
        lifo.getPosicao( input("Digite o que deseja procurar na pilha: ") )
    elif op == 0:
        print("Bye-bye!!!")
    else: 
        print("Opção inválida")