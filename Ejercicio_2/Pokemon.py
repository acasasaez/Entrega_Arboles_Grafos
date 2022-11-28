#En este caso se nos ofrece un archivo csv D con los datos de 700 pokemons, aproximadamente, se nos pide que creemos 3 árboles
# A partir de sus nombres
# A partir de sus tipos
# A partir de sus números


import pandas as pd 
d_pokemon = pd.read_csv("/Users/andre/OneDrive/Escritorio/Programación/Entrega_Arboles_Grafos/Ejercicio_2/pokemon.csv", sep = ",")

#Creamos nuestros pokemons que serán nuestros nodos aunque cada árbol los identificará con un atributo distinto.
class Pokemon (): 
    def __init__(self):
        self.nombre = ""
        self.numero = 0
        self.tipo1 = None
        self.tipo2 = None
        self.debilidad = 0

# Una vez que ya había creado ayer las tres clases árbol ahora empezamos con sus funciones. 
# La primera, que es la inicialización de los pokemon, será igual para los tres árboles. Esta función lo que hace es atribuir las caracteristicas de los pokemons que conformarán nuestro árbol.
        
        
class  ArbolNombre ():
    def __init__(self, pokemons ):
        self.Nodos = []
        self.pokemons = pokemons
    
    def inicializarPokemon(self):
        for i in range(0, len(self.pokemons)):
            pokemon = Pokemon()
            pokemon.nombre = self.pokemons.iloc[i,1]
            pokemon.numero = self.pokemons.iloc[i,0]
            pokemon.tipo1 = self.pokemons.iloc[i,2]
            pokemon.tipo2 = self.pokemons.iloc[i,3]
            pokemon.debilidad = self.pokemons.iloc[i,4]
            self.Nodos.append(pokemon)

    def ObtenerNombre(self):
        Nombre = []
        for i in range (0, len(self.Nodos)):
             Nombre.append(self.Nodos[i].nombre) 
        return Nombre

class ArbolTipo():
    def __init__(self, pokemons ):
        self.Nodos = []
        self.pokemons = pokemons

    def inicializarPokemon(self):
        for i in range(0, len(self.pokemons)):
            pokemon = Pokemon()
            pokemon.nombre = self.pokemons.iloc[i,1]
            pokemon.numero = self.pokemons.iloc[i,0]
            pokemon.tipo1 = self.pokemons.iloc[i,2]
            pokemon.tipo2 = self.pokemons.iloc[i,3]
            pokemon.debilidad = self.pokemons.iloc[i,4]
            self.Nodos.append(pokemon)
            

        
class ArbolNumero():
    def __init__(self, pokemons ):
        self.Nodos = []
        self.pokemons = pokemons

    def inicializarPokemon(self):
        for i in range(0, len(self.pokemons)):    
            pokemon = Pokemon()
            pokemon.nombre = self.pokemons.iloc[i,1]
            pokemon.numero = self.pokemons.iloc[i,0]
            pokemon.tipo1 = self.pokemons.iloc[i,2]
            pokemon.tipo2 = self.pokemons.iloc[i,3]
            pokemon.debilidad = self.pokemons.iloc[i,4]
            self.Nodos.append(pokemon)

arbol = ArbolNombre(d_pokemon)
arbol.inicializarPokemon()
print(arbol.ObtenerNombre())