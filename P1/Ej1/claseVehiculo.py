class Vehiculo:
    __marca : str
    __modelo : str
    __patente : str
    __importedeAlquiler: float
    __kilometros: int

    def __init__(self, marca = '', modelo = '', patente = '', importedeAlquiler = 0, kilometros = 0):
        self.__marca = marca
        self.__modelo = modelo
        self.__patente = patente
        self.__importedeAlquiler = importedeAlquiler
        self.__kilometros = kilometros

    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getPatente(self):
        return self.__patente
    
    def getImporteDeAlquiler(self):
        return self.__importedeAlquiler
    
    def getKilometros(self):
        return self.__kilometros
    
    def getImporteTotal():
        pass
    
    def __str__(self):
        return self.__marca + " " + self.__modelo + " " + self.__patente + " $" + str(self.__importedeAlquiler) + " " + str(self.__kilometros)