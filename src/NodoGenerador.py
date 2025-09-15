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
        self.mensajes_esperados = len(vecinos) 

    def tostring(self):
        return f"ID: {self.id_nodo}, Padre: {self.padre}, Hijos: {self.hijos}"

    
    def genera_arbol(self, env):
        """
        Construye un árbol generador desde el nodo 0.
        """
        if self.id_nodo == 0: 
            self.padre = self.id_nodo #Se define el nodo padre 
            self.mensajes_esperados = len(self.vecinos) #Se esperan los mensajes BACK de los vecinos
            for vecino in self.vecinos:
                yield env.timeout(TICK) #Simula el tiempo de envio
                self.canal_salida.envia((GO_MSG, self.id_nodo), [vecino]) #Se envia Go a los vecinos
        else:
            self.padre = None #No hay nodo padre

        while True: #Bucle donde se recibe mensajes
            msg = yield self.canal_entrada.get() #Se espera recibir el mensaje
            tipo, remitente = msg #Se ve el tipo de mensaje y remitente

            if tipo == GO_MSG: #Si el tipo recibido es Go
                if self.padre is None: #Se define el padre
                    self.padre = remitente
                    self.mensajes_esperados = len(self.vecinos) - 1 

                    if self.mensajes_esperados == 0: 
                        yield env.timeout(TICK) 
                        self.canal_salida.envia((BACK_MSG, self.id_nodo), [self.padre]) #Cuando no hay vecinos, envia BACK
                    else:
                        for vecino in self.vecinos: #Envia GO a todos los vecinos menos al padre
                            if vecino != self.padre:
                                yield env.timeout(TICK)
                                self.canal_salida.envia((GO_MSG, self.id_nodo), [vecino])
                else: #Si el tipo de mensaje es BACK
                    yield env.timeout(TICK) 
                    self.canal_salida.envia((BACK_MSG, None), [remitente]) #Envia BACK vacio

            elif tipo == BACK_MSG: #Si el mensaje BACK es de un hijo
                self.mensajes_esperados -= 1 #Se reduce el contador de mesajes esperados
                if remitente is not None:
                    self.hijos.append(remitente) #Lo guarda en el hijo que respondio (remitente)

                if self.mensajes_esperados == 0 and self.padre != self.id_nodo: #Si ya se recibio todos los mensajes esperados
                    yield env.timeout(TICK)
                    self.canal_salida.envia((BACK_MSG, self.id_nodo), [self.padre]) #Envia BACK al padre
