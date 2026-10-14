from No import No

class Arvore:

    def __init__(self):
        self.raiz = None

    def add(self, raiz: No, valor):
        if raiz is None:
            nodo = No( valor )
            if self.raiz is None:
                self.raiz = nodo
            return nodo
        if valor < raiz.dado:
            raiz.esq = self.add( raiz.esq, valor )
        
        if valor > raiz.dado:
            raiz.dir = self.add( raiz.dir, valor )

        return raiz
    
    def imprimirEmOrdem(self , raiz : No ):
        if raiz != None:
            self.imprimirEmOrdem( raiz.esq )
            print( raiz.dado , end = " - ")
            self.imprimirEmOrdem( raiz.dir )

    def imprimirPreOrdem(self , raiz : No ):
        if raiz != None:
            print( raiz.dado , end = " - ")
            self.imprimirPreOrdem( raiz.esq )
            self.imprimirPreOrdem( raiz.dir )

    def imprimirPosOrdem(self , raiz : No ):
        if raiz != None:
            self.imprimirPosOrdem( raiz.esq )
            self.imprimirPosOrdem( raiz.dir )
            print( raiz.dado , end = " - ")

    def imprimirReverso(self , raiz : No ):
        if raiz != None:
            self.imprimirReverso( raiz.dir )
            print( raiz.dado , end = " - ")
            self.imprimirReverso( raiz.esq )
    