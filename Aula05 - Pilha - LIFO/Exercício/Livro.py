class Livro:

    def __init__(self, titulo, autor, qntd_pag):
        self.titulo = titulo
        self.autor = autor
        self.qntd_pag = qntd_pag
        self.prox = None

    def __str__(self):
        return f""" 
Livro: {self.titulo} |
Autor: {self.autor}  |
Quantidade de páginas: {self.qntd_pag} """