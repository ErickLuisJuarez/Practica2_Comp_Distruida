import simpy
from Nodo import *
from Canales.CanalBroadcast import *
from Auxiliares import *

TICK = 1
class NodoBusqueda(Nodo):
    def __init__(self, id_nodo,vecinos,cantidad_nodos ,canal_entrada, canal_salida,mensaje=None):
        '''Inicializamos el nodo.'''
        self.id_nodo = id_nodo
        self.vecinos = vecinos
        self.cantidad_nodos =  cantidad_nodos
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida
        self.arr = []
        self.contenido = False 
    

    def toString(self):
        return f"Id_nodo = {self.id_nodo},Vecinos: {self.vecinos},array: {self.arr},estado: {self.contenido}"

    def busqueda(self,env,arr,elemento):

        if self.id_nodo == 0 :
            segmento = cuadricula(arr, self.cantidad_nodos + 1) #Nodo coordinador que divide el arreglo entre 2 nodos 
            self.arr = segmento[0]
            
            for e in self.arr: # Para buscar su propio segmento 
                if e == elemento:
                    self.contenido = True
                    break

            for i in range(1, len(segmento)):
                yield env.timeout(TICK)
                self.canal_salida.envia(("GO", segmento[i], elemento), [i])

        while True :
            orden,arr_,elem = yield self.canal_entrada.get()
            self.arr = arr_
            
            if orden == "GO" :
                encontrado = False 
                for e in arr_ :
                    if e == elem :
                        encontrado = True 
                        break

                if encontrado :
                    msg =  ("FOUND",arr_,elemento)  
                    self.contenido = True 
                    self.canal_salida.envia(msg,[0])
                else:
                    msg =  ("NOT_FOUND",arr_,elemento)  
                    self.contenido = False
                    self.canal_salida.envia(msg,[0])

            else:
                if orden == "FOUND":
                    self.contenido = True 
