from claseVehiculo import Vehiculo

class DeCarga(Vehiculo):
    __pesoDeCarga : int

    def __init__(self, marca='', modelo='', patente='', importedeAlquiler=0, kilometros=0, pesoDeCarga = 0):
        super().__init__(marca, modelo, patente, importedeAlquiler, kilometros)
        self.__pesoDeCarga = pesoDeCarga

    def getPesoDeCarga(self):
        return self.__pesoDeCarga
    
    def getImporteTotal(self):
        adicionalKm = 0
        if self.getKilometros() > 100:
            adicionalKm = (self.getKilometros()-100) // 10 * (self.getImporteDeAlquiler()*5/100) 
        adicionalKg = 0
        if self.getPesoDeCarga() > 500:
            adicionalKg = (self.getPesoDeCarga()-500) // 100 *(self.getImporteDeAlquiler()*10/100)

        importetotal = self.getImporteDeAlquiler() + adicionalKg + adicionalKm
        
        return  importetotal

    def __str__(self):
        return super().__str__() + " " + str(self.__pesoDeCarga)
    
