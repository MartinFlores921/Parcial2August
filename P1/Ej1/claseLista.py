from claseNodo import Nodo

class Lista:
    __comienzo : Nodo
    
    
    __actual : Nodo
    __indice : int
    __tope : int

    def __init__(self):
        self.__comienzo = None
        
        self.__actual = None
        self.__indice = 0
        self.__tope = 0


    def __iter__(self):
        self.__actual = self.__comienzo
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato

    def agregarVehiculo(self, vehiculo):
        nodo = Nodo(vehiculo)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        
        self.__actual = nodo
        self.__tope +=1

    def mostrarrrrrrrVehiculosAsientos(self):
        aux = self.__comienzo
        while aux != None:
            if(aux.getDatoAsientos() > 6):
                print(aux.getDato())
            aux = aux.getSiguiente()


    def contarSegunnnnnMarca(self, marca):
        aux = self.__comienzo
        contador = 0
        while aux != None:
            if aux.esDeCarga() and aux.getDatoMarca() == marca:
                contador += 1
            aux = aux.getSiguiente()

        return contador
    
    def mostrarrrrrTodosVehiculos(self):
        print("\t\tMarca\t\tModelo\t\tTipo de vehiculo\t\tKilometros a recorrer\t\tTotal alquiler")
        aux = self.__comienzo
        while aux != None:
            print(aux.mostrarEnFormato())
            aux = aux.getSiguiente()