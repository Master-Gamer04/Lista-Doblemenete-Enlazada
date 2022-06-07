from ListaCircular import ListaCircular

lista = ListaCircular()

lista.agregarFin('7')
lista.agregarFin('2')
lista.agregarFin('10')
lista.agregarFin('40')
lista.agregarFin('5')
lista.agregarFin('6')
lista.agregarFin('73')
lista.agregarFin('21')

lista.print_list()

numero = input('Ingrese el numero que desea ver en la lista: ')

lista.buscadorNumero(numero)