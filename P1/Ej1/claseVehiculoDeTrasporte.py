from claseVehiculo import Vehiculo

class DeTransporte(Vehiculo):
    __cantidadAsientos : int

    def __init__(self, marca='', modelo='', patente='', importedeAlquiler=0, kilometros=0, cantidadAsientos = 0):
        super().__init__(marca, modelo, patente, importedeAlquiler, kilometros)
        self.__cantidadAsientos = cantidadAsientos

    def getCantidadAsientos(self):
        return self.__cantidadAsientos
    

    def getImporteTotal(self):
        adicionalKm = 0
        if self.getKilometros() > 100:
            adicionalKm = (self.getKilometros()-100) // 10 * (self.getImporteDeAlquiler()*1/100) 
        adicionalAsientos = 0
        if self.getCantidadAsientos() > 4:
            adicionalAsientos = self.getImporteDeAlquiler()*1/100

        importetotal = self.getImporteDeAlquiler() + adicionalAsientos + adicionalKm
        
        return  importetotal


    def __str__(self):
        return super().__str__() + " " + str(self.__cantidadAsientos)