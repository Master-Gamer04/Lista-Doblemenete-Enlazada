class Nodo:

    def __init__(self, numero) -> None:
        self.numero = numero
        self.siguiente = None
        self.anterior = None

    #####################################################
    def getNumero(self):
        return self.numero
    
    def setNumero(self, numero):
        self.numero = numero