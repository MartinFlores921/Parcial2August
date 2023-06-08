from claseVehiculoDeCarga import DeCarga
from claseVehiculoDeTrasporte import DeTransporte
from manejador import manejadorVehiculos

if __name__ == "__main__":

    vehiculo1 = DeCarga("Ford", "Fiesta", "ABC123", 20000, 200, 800)
    vehiculo2 = DeTransporte("Chevrolet", "Corsa", "MUP555", 30000, 200, 8)
    vehiculo3 = DeCarga("Ford", "Focus", "NIB214", 25000, 250, 700)
    vehiculo4 = DeTransporte("Mercedes Benz", "SL-500", "AA253BB", 40000, 500, 8)

    manejador = manejadorVehiculos()
    manejador.agregarElemento(vehiculo1)
    manejador.agregarElemento(vehiculo2)
    manejador.agregarElemento(vehiculo3)
    manejador.agregarElemento(vehiculo4)

    manejador.mostrarVehiculosAsientos()

    marca = "Ford"
    c = manejador.contarSegunMarca(marca)
    print("La cantidad de vehiculos de la marca {} es: {}".format(marca,c))

    manejador.mostrarElementos()
