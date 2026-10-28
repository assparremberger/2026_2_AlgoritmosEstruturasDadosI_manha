from Carro import Carro
from Fila import Fila

class Arvore:

    def __init__(self):
        self.raiz : Carro = None

    def add(self, raiz: Carro, newCar : Carro ):
        if raiz is None:
            if self.raiz is None:
                self.raiz = newCar
            return newCar
        if newCar.placa < raiz.placa:
            raiz.esq = self.add( raiz.esq, newCar )
        
        if newCar.placa > raiz.placa:
            raiz.dir = self.add( raiz.dir, newCar )

        return raiz
    
    def imprimirEmOrdem(self , raiz : Carro ):
        if raiz != None:
            self.imprimirEmOrdem( raiz.esq )
            print( raiz )
            self.imprimirEmOrdem( raiz.dir )

    def imprimirPreOrdem(self , raiz : Carro ):
        if raiz != None:
            print( raiz )
            self.imprimirPreOrdem( raiz.esq )
            self.imprimirPreOrdem( raiz.dir )

    def imprimirPosOrdem(self , raiz : Carro ):
        if raiz != None:
            self.imprimirPosOrdem( raiz.esq )
            self.imprimirPosOrdem( raiz.dir )
            print( raiz )

    def imprimirReverso(self , raiz : Carro ):
        if raiz != None:
            self.imprimirReverso( raiz.dir )
            print( raiz )
            self.imprimirReverso( raiz.esq )

    def imprimirEmNivel(self, raiz: Carro):
        if raiz == None:
            return
        fila = Fila()
        fila.add( raiz )

        while fila.inicio != None:
            tam = fila.tamanho
            for _ in range( tam ):
                atual = fila.remover()
                print( atual )
                if atual.esq != None:
                    fila.add( atual.esq )
                if atual.dir != None:
                    fila.add( atual.dir )
            print("")


    