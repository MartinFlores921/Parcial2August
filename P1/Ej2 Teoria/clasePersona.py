class Persona:
    __dni : str
    __apellido : str
    __nombre : str
    __domicilio : object


    def __init__(self, dni, apellido, nombre, domicilio):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__domicilio = domicilio

    def getDni(self):
        return self.__dni
    
    def getApellido(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre
    
    def getDomicilio(self):
        return self.__domicilio
    
    def __str__(self):
        return "\t"+ self.__dni + " " + self.__apellido + " " + self.__nombre + " Domicilio: " + str(self.__domicilio)
    