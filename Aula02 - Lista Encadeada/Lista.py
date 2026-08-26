from No import No

class Lista:

    def __init__(self):
        self.inicio = None

    # Lista Encadeada por ordem de chegada
    def add(self, valor):
        nodo = No(valor)
        if self.inicio is None:
            self.inicio = nodo
        elif self.inicio.prox == None:
            self.inicio.prox = nodo
        else:
            aux = self.inicio.prox
            while aux.prox != None:
                aux = aux.prox
            aux.prox = nodo
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
            
