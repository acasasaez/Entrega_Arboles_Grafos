
#Se nos pide crear un arbol Huffman a partir de la siguiente tabla de frecuencias que nos permita codificar y decodificar mensajes.
#TABLA: 0.2 F: 0.17 1: 0.13 3: 0.21 0: 0.05 M: 0.09 t: 0.15
# ARBOL HUFFMAN:
#            1
#           /  \
#          /    \
#       0.41     0.59
#       /  \     /   \
#  0.20 0.21    0.27   0.32
#             /  \      /  \
#          0.13 0.14   0.15 0.17  
#                 /  \
#              0.05  0.09 


# Creamos nuestra clase nodo 
class Nodo ():
   probabilidad = 0.0
   simbolo = ""
   codificacion = ""
   a = False

#Creamos nuestra clase Arbol de Huffman
class ArbolHuffman():
   def __init__(self, Probabilidades={}): #
        self.Arbol = None #Rrecordamos quel el arbol como nuestros TDA inicia siendo None, pasaremos a crearlo posteriormente 
        self.Raiz =None
        self.Nodos = []
        self.Probabilidades = Probabilidades #Diccionario con simbolos y probabilidades 
        self.diccionarioCodificacion = {} # resultado binario
       
   def inicializarNodo(self): #Inicializamos los nodos con los simbolos y probabilidades
         for simbolo in self.Probabilidades.keys():
            nodo = Nodo() # Cada nodo es una instancia de la clase Nodo
            nodo.simbolo = simbolo #Asignamos los simbolos a los nodos que serán clave o la base de nuestro aáebol ( a partir de los cueles lo iremos construyendo )
            nodo.probabilidad = self.Probabilidades[simbolo] #Asignamos las probabilidades a los nodos
            self.Nodos.append(nodo) #Añadimos los nodos a la lista de nodos
            
   def NododeMinimaProb(self):
        ProbabilidadMaxima = 1.0 
        Restamaxima = -1

        for i in range(0, len(self.Nodos)):
            if (self.Nodos[i].probabilidad < ProbabilidadMaxima and
                (not self.Nodos[i].a)):
                ProbabilidadMaxima = self.Nodos[i].probabilidad
                Restamaxima = i

        if Restamaxima != -1:
            self.Nodos[Restamaxima].a = True

        return Restamaxima
#Creamos nuestro arbol de Huffman
   def CrearArbol (self):
       #Para eso empezamos por busscar los nodos con menor probabilidad
       min1 = self.NododeMinimaProb()
       min2 = self.NododeMinimaProb()

       while min2 != -1 and min2 != -1: #Mientras no se acaben los nodos
        nodo = Nodo () #Creamos un nuevo nodo que será el nodo padre
        nodo.simbolo = ""
        nodo.codificacion = ""
        prob1 = self.Nodos[min1].probabilidad
        prob2 = self.Nodos[min2].probabilidad
        nodo.probabilidad =prob1 + prob2 #Por ello su probabilidad será la suma de las probabilidades de sus hijos
        nodo.a = False
        self.Nodos.append(nodo) #Añadimos el nodo a la lista de nodos
        #Realizamos la codificación vinaria de los nodos
        if prob1 >= prob2:
            self.Nodos[min1].codificacion = "0"
            self.Nodos[min2].codificacion = "1"
        else:
            self.Nodos[min1].codificacion = "1"
            self.Nodos[min2].codificacion = "0"
            print ("Nodo padre: ", nodo.probabilidad) 
            print ("Nodo hijo izquierdo: ", self.Nodos[min1].probabilidad)
            print ("Nodo hijo derecho: ", self.Nodos[min2].probabilidad)
        min1 = self.NododeMinimaProb()
        min2 = self.NododeMinimaProb()
    


    #Un Arbol Huffman es un arbol binario que nos permitirá  codificacición y decodificación de mensajes a partir tablas de frecuencias. 
    #Para poder crear nuestreo árbol el primer paso será crear nuestra clase nodo que será la base de nuestro árbol y que contendrán la información ( simbolo y probabilidad) de cada nodo.
    #Posteriormente creamos la clase del arbol de Huffman que trabajará de la siguiente manera:
        #En su contrusctor pasaremos por parámetro un diccionario conn los símbolos y probabilidades de nuestro problema. 
        # A continuación, crearemos una lista vacía donde almacenaremos nuestros nodos
        #Crearemos otra variable, de tipo diccionario, que emplearemos más tarde para poder recoger el codigo binario que codificará nuestros mensajes un a vez realizado el árbol

        #El siguiente paso es In icializar los nodos de nuestro árbol de huffman
        #Para ello creamos la función inicializar nodo. 
        #Con esta recorreremos el dicccionario (probabilidades) y por cada clave valor crearemos una instancia de nodo ( siendo clave su simbolo y valor su probabilidad) y lo añadiremos a nuestra lista de nodos)

        #Una vez que tenemos los nodos base de nuestro árbol pasamos a crear la función que busque las menores probabilidades (INTERNET)

        #Una vez que tenemos los nodos con menor probabilidad pasamos a crear el árbol de Huffman
         

        
        #Para esto empezamos buscando las probabbilidades mínimas de nuestro árbol y las almacenamos en las variables min1 y min2.
        # # Hasta que no se terminen los nodos, será necesario crear nodos intermedios que nos permitan construir el árbol desde nuestras probabilidades hasta la raiz. probabilidad 1 
        ##Añadimos nuestro nodo as la lista de nodos y codificamos los nodos hijos
        #recalculamos los nodos de mínima probabilidad de nuestra lista de nodos 

        #Una vez que tenemos nuestro árbol procedemos a crear el diccionario que guarde el código binario de nuestros caracteres 
        #Acabar de programar 
        #Arrecglar las probabilidades de los nodos
#
#Hacer menu, poner bonito
dic = {"A": 0.2, 
        "F": 0.17,
          "1": 0.13, 
          "3": 0.21, 
          "0": 0.05, 
          "M": 0.09, 
          "T": 0.15}
arbol = ArbolHuffman(dic)
arbol.inicializarNodo()
arbol.CrearArbol()
