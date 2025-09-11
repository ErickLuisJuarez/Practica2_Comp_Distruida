import simpy
from Nodo import *
from Canales.CanalBroadcast import *

TICK = 1
GO_MSG = "GO"
BACK_MSG = "BACK"

class NodoGenerador(Nodo):
    '''Implementa la interfaz de Nodo para el algoritmo de flooding.'''
    def __init__(self, id_nodo, vecinos, canal_entrada, canal_salida):
        '''Inicializamos el nodo.'''
        self.id_nodo = id_nodo
        self.vecinos = vecinos
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida
        
        # Atributos propios del algoritmo
        #self.padre = None if id_nodo != 0 else id_nodo # Si es el nodo distinguido, el padre es el mismo 
        self.padre = None
        self.hijos = list()
        self.mensajes_esperados = len(vecinos) # Cantidad de mensajes que esperamo

    def tostring(self):
        return f"ID: {self.id_nodo}, Parent: {self.padre}, Children: {self.hijos}"

    
    def genera_arbol(self, env):
        if self.id_nodo == 0:
            self.padre = self.id_nodo
            yield env.timeout(TICK)
            self.canal_salida.envia((GO_MSG, self.id_nodo), self.vecinos)

        while True:
            msg = yield self.canal_entrada.get()
            if msg[0] == GO_MSG:
                if self.padre is None:
                    self.padre = msg[1]
                    hijos = [v for v in self.vecinos if v != self.padre]
                    self.hijos = hijos
                    self.canal_salida.envia((GO_MSG, self.id_nodo), hijos)
        



                    
                    





                    







                


