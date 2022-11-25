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

import os 
# Creamos nuestra clase nodo 
class Nodo ():
   probabilidad = 0.0
   simbolo = ""
   codificacion = ""

#Creamos nuestra clase Arbol de Huffman
class ArbolHuffman():
   def __init__(self, Arbol= None, Raiz=None, Nodos = [], Probabilidades={}, diccionarioCodificacion={}):
        self.Arbol = Arbol
        self.Raiz = Raiz
        self.Nodos = Nodos
        self.Probabilidades = Probabilidades
        self.diccionarioCodificacion = diccionarioCodificacion
       
     
    