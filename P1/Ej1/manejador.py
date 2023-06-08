from claseLista import Lista
from claseVehiculoDeCarga import DeCarga
from claseVehiculoDeTrasporte import DeTransporte


class manejadorVehiculos:
    __listaVehiculos : Lista

    def __init__(self):
        self.__listaVehiculos = Lista()

    def agregarElemento(self,vehiculo):
        self.__listaVehiculos.agregarVehiculo(vehiculo)

    def mostrarElementos(self):
        for vehiculo in self.__listaVehiculos:
            print(vehiculo)

    def mostrarVehiculosAsientos(self):
        for vehiculo in self.__listaVehiculos:
            if isinstance(vehiculo,DeTransporte) and vehiculo.getCantidadAsientos() > 6:
                print(vehiculo)

    def contarSegunMarca(self,marca):
        c=0
        for vehiculo in self.__listaVehiculos:
            if vehiculo.getMarca() == marca and isinstance(vehiculo,DeCarga):
                c +=1

        return c