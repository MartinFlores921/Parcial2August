from claseVehiculoDeCarga import DeCarga
from claseVehiculoDeTrasporte import DeTransporte
from claseVehiculo import Vehiculo

class Nodo:
    __vehiculo : Vehiculo
    __siguiente : object

    def __init__(self, vehiculo):
        self.__vehiculo = vehiculo
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__vehiculo
    
    def getDatoAsientos(self):
        c = 0
        if isinstance(self.__vehiculo, DeTransporte):
            c = self.__vehiculo.getCantidadAsientos()
        else:
            c = False
        return c
        
    def esDeCarga(self):
        band = False
        if isinstance(self.__vehiculo, DeCarga):
            band = True
        return band
    
    def getDatoMarca(self):
        return self.__vehiculo.getMarca()
    
    def getTipo(self):
        tipo : str
        if isinstance(self.__vehiculo, DeCarga):
            tipo = "Vehiculo de Carga"
        elif isinstance(self.__vehiculo,DeTransporte):
            tipo = "Vehiculo de Transporte"
        return tipo

    def mostrarEnFormato(self):
        cadena = "{:>20}\t{:>15}\t{:>25}\t{:>20}\t{:>25}$".format(self.__vehiculo.getMarca(),self.__vehiculo.getModelo(),self.getTipo(),str(self.__vehiculo.getKilometros()),str(self.__vehiculo.getImporteTotal()))
        return cadena