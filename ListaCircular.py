from Nodo import Nodo

class ListaCircular:
    
    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None

    def vacio(self):
        return self.primero == None

    def agregarFin(self,numero):
        if self.vacio():
            self.primero = self.ultimo = Nodo(numero)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(numero)
            self.ultimo.anterior = aux
        self.unirNodos()

        # Imprimir Lista
    def print_list(self):
        if not self.vacio():
            aux = self.primero
            while aux != None:
                print('| {} |'.format(str(aux.numero)))
                aux = aux.siguiente
                if aux == self.primero:
                    break
        else:
            return None

    def buscadorNumero(self,opcion):
        aux = self.primero
        while aux != None:
            if aux.numero == opcion:
                print('| Anterior: {} | Acutal: {} | Siguiente: {} |'.format(aux.anterior.numero,aux.numero, aux.siguiente.numero))
                break
            elif aux == self.ultimo:
                if aux.numero == opcion:
                    print('| Anterior: {} | Acutal: {} | Siguiente: {} |'.format(aux.anterior.numero,aux.numero, aux.siguiente.numero))
                    break
                else:
                    print('El numero no esta en la lista')
                    break
            aux = aux.siguiente

    def unirNodos(self):
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero