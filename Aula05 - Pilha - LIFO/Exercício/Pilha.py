from Livro import Livro

class Pilha:
    def __init__(self):
        self.topo = None


#Adicionar livro na pilha

    def add(self, book):
        if self.topo != None:
            book.prox = self.topo
        self.topo = book
        self.imprimir()

#Imprimir pilha de livros

    def imprimir(self):
        print("------ Pilha de Livros ------")
        if self.topo == None:
            print("A pilha está vazia")
        else:
            aux = self.topo
            while aux:
                print( aux )
                aux = aux.prox
            print("-----------------------------")

#remover livro da pilha

    def remover (self):
        if self.topo != None:
            aux = self.topo
            self.topo = self.topo.prox
            print(f"{aux.titulo} removido da pilha!")
            del(aux)
        self.imprimir()

#pegar posicao do livro

    def getPosicao(self, valor):
        if self.topo == None :
            print( "Pilha Vazia" )
        else:
            cont = 1
            encontrou = False
            aux = self.topo
            while aux != None:
                if aux.titulo == valor:
                    encontrou = True
                    break
                else:
                    cont += 1
                    aux = aux.prox
            if  encontrou:
                print(f'Livro: {valor} encontrado na posição {cont}')
            else:
                print(f'Livro: {valor} não encontrado na pilha' )



    def buscar_autor(self, autor):
        if self.topo == None:
            print("Pilha vazia")

        else:
            aux = self.topo
            cont = 0
            while aux:
                if aux.autor == autor:
                    print(aux.titulo)
                    cont +=1 
                aux = aux.prox

            if cont == 0:
                print("Nenhum livro encontrado do autor " + autor)
            else:
                print( cont , " livros encontrados!")

