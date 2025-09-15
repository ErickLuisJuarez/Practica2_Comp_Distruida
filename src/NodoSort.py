import simpy
from Nodo import *
from Canales.CanalBroadcast import *
from Auxiliares import *

class NodoSort(Nodo):
    def __init__(self, id_nodo,vecinos,cantidad_nodos,canal_entrada, canal_salida,mensaje=None):
        '''Inicializamos el nodo.'''
        self.id_nodo = id_nodo
        self.vecinos = vecinos
        self.cantidad_nodos =  cantidad_nodos
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida
        self.arr = []

    def ordernar(self,env,arr):
        if self.id_nodo == 0:  # nodo coordinador
            n = len(arr)
            p = self.cantidad_nodos
            tam = n // p  # division entera entre tamano del arreglo y numero de nodos

            # vamos enviando pedazos del arreglo a los trabajadores
            for i in range(1, p):
                izq = (i-1)*tam
                der = i*tam
                Ai = arr[izq:der]
                self.canal_salida.envia(("pedazo", Ai), [i])

            # el coordinador se quedara con el resto
            izq = (p-1)*tam
            der = n
            A0 = arr[izq:der]
            A0.sort()

            # juntamos los resultados
            listas = [A0]
            for i in range(1, p):
                mensaje = yield self.canal_entrada.get()
                _, Ai_ord = mensaje
                listas.append(Ai_ord)

            # k merge
            resultado = k_merge(listas)
            self.arr = resultado   # guardamos el arreglo ordenado

        else:  # nodo trabajador
            # el nodo espera que le manden un pedazo
            mensaje = yield self.canal_entrada.get()
            _, Ai = mensaje
            Ai.sort()

            # se envia al coordinador
            self.canal_salida.envia(("ordenado", Ai), [0])