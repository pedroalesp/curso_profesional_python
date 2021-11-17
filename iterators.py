class EbenNumbers:
    # """Clase que implementa un iterador de todos los números pares o los 
    #     números pares hasta un máximo"""

    #Constructor:
    def __init__(self, max=None):
        self.max = max 
        # """El atributo max de este objeto que posteriormente
        #     va a ser un iterador, será igual al parámetro max 
        #     que me llega del constructor"""
    
    def __iter__(self):
        self.num = 0
        return self
        # """En este caso, el atributo que necesitamos para el iterador son cada uno de los  números de la iteración
        #     y como comenzamos en 0, decimos que self.num = 0,
        #     es decir, el primer número par
        # El atributo num es el valor que va por cada vuelta del iterador"""

    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num +=2
            return result
        # """Con este condicional, creamos la variable result que vamos a mostrar
        # y le vamos sumando 2 al atributo num para tener el valor par en la 
        # siguiente vuelta"""
        else:
            # return StopIteration
            # """Si nos encontramos con el máximo
            # elevamos un error para detener al iterador"""