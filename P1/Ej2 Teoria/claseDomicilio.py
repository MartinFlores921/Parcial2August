class Domicilio:
    __calle : str
    __numero : int

    def __init__(self,calle,numero):
        self.__calle = calle
        self.__numero = numero

    def getCalle(self):
        return self.__calle
    
    def getNumero(self):
        return self.__numero
    

    def __str__(self):
        return self.__calle + " " + str(self.__numero)