from No import No

class Pilha:

    def __init__(self):
        self.topo = None

    def add(self, valor ):
        nodo = No( valor )
        if self.topo != None:
            nodo.prox = self.topo
        self.topo = nodo
        self.imprimir()

    def imprimir(self):
            print("-------- Pilha - LIFO --------")
            if self.topo == None:
                print("Pilha Vazia")
            else:
                aux = self.topo
                while aux:
                    print( aux.dado )
                    aux = aux.prox
            print("------------------------------------------------------")

    def remove(self):
        if self.topo != None:
            aux = self.topo
            self.topo = self.topo.prox  
            print( aux.dado + " removido da pilha!")
            del( aux )   
        self.imprimir()

    # Função adicional
    def getPosicao(self, valor):
        if self.topo == None :
            print( "Pilha Vazia" )
        else:
            cont = 1
            encontrou = False
            aux = self.topo
            while aux != None:
                if aux.dado == valor:
                    encontrou = True
                    break
                else:
                    cont += 1
                    aux = aux.prox
            if  encontrou:
                print(f'Valor: {valor} encontrado na posição {cont}')
            else:
                print(f'Valor: {valor} não encontrado na pilha' )
            