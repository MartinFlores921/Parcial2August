from claseDomicilio import Domicilio
from clasePersona import Persona

if __name__ == "__main__":

    domicilio1 = Domicilio("25 de mayo Este", "210")
    persona1 = Persona("44922842", "Gomez", "Gonzalo", domicilio1)
    persona2 = Persona("38904021", "Gomez", "Manuel", domicilio1)
    persona3 = Persona("35093013", "Gomez", "Ana Maria", domicilio1)


    domicilio2 = Domicilio("Avenida Libertador Oeste", "403")
    persona4 = Persona("65463127", "Martinez", "Mauro", domicilio2)
    persona5 = Persona("35674398", "Fernandez", "Oscar", domicilio2)


    print(persona1)
    print(persona2)
    print(persona3)
    print(persona4)
    print(persona5)