from No import No

class Lista:

    def __init__(self):
        self.inicio = None

    # Lista Encadeada por ordem CRESCENTE
    def add(self, valor):
        nodo = No(valor)

        if self.inicio is None:
            self.inicio = nodo
        else:
            if nodo.dado < self.inicio.dado:
                nodo.prox = self.inicio
                self.inicio = nodo
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux :
                    if nodo.dado < aux.dado:
                        ant.prox = nodo
                        nodo.prox = aux
                        break
                    else:
                        ant = aux
                        aux = aux.prox
                if aux == None:
                    ant.prox = nodo
        self.imprimir()

    def imprimir(self):
        print("-------- Lista Encadeada por ordem de chegada --------")
        if self.inicio == None:
            print("Lista Vazia")
        else:
            aux = self.inicio
            while aux:
                print( aux.dado )
                aux = aux.prox
        print("------------------------------------------------------")
            
    def remover(self, valor):
        if self.inicio is None:
            print("A lista está vazia")
        else:
            removido = False
            if self.inicio.dado == valor:
                aux = self.inicio
                self.inicio = self.inicio.prox
                del( aux )
                removido = True
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux :
                    if aux.dado == valor:
                        ant.prox = aux.prox
                        del( aux )
                        removido = True
                        break
                    else: 
                        ant = aux
                        aux = aux.prox

            if removido:
                print( "Item (",valor, ") removido com sucesso!")
            else: 
                print( "Item (",valor, ") não encontrado!")

            self.imprimir()
                    
