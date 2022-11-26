#En este caso se nos ofrece un archivo csv con los datos de 700 pokemons, aproximadamente, se nos pide que creemos 3 árboles
# A partir de sus nombres
# A partir de sus tipos
# A partir de sus números
#Nos encontramos ante un problema que podemos enfrentar con un avl y un algoritmo de búsqueda binaria
#Empezaremos creando un TDA, ya que ñas columnas que emplearemos de nuestro archivo csv las manejaremos como atributos de nuestro TDA
class Cola ():
    def __init__(self):
        self.dato =[] # que son el conjunto abstracto de datos que manejamos
        self.cabeza = 0 # aue es el numero elementos que salen de nuestra cola
        self.cola = 0 #numero de elementos que entran a nuestra cola
    
    def esta_vacia(self): #resuñtado de tipo booleano. si el numero de elementos que entra en nuestra cola es igual al que sale entonces nuestra cola estarña vacía-
        if self.cabeza == self.cola:
            return True
        else:
            return False
        
    def añadirElemento(self, elemento): #añadimos un elemento a nuestra cola
        self.dato.append(elemento)
        self.cola += 1 #la variable que guarda el nuumero de elementos que entran a nuestra cola aumenta en 1 unidad

    def sacarElemento(self): #sacamos un elemento de nuestra cola
        ret = self.dato[self.cabeza]
        self.cabeza += 1
        return ret #retornamos el elemento que sacamos de nuestra cola
    def tamañoCola(self):
        return self.cola - self.cabeza 
    