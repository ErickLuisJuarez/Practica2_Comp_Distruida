def k_merge(listas):
    """
    Recibe una lista de k listas ordenadas
    y regresa una sola lista con todos los elementos

    """
    
    if not listas: #Si la lista está vacía, devolvemos []
        return []    

    resultado = [] 
    for lista in listas:
        resultado.extend(lista) #Se agrega cada sublista completa al resultado
    
    resultado.sort() #Se ordenan los elementos 
    return resultado #Devuelve la lista ordenada

def cuadricula(arr,cantidad_nodos):
    longitud = len(arr) #Numero total de elementos
    base = longitud // cantidad_nodos #Tamaño base de cada segmeneto
    residuo = longitud % cantidad_nodos #Residuo de la division

    cuadricula = [] #Lista de los segmentos
    inicio = 0 #Indice del inicio del siguiente segmento
    for i in range(cantidad_nodos): #Iteracion sobre la cantidad de nodos
        tamano = base +(1 if i < residuo else 0) #Algunos segmentos tiene residuos
        cuadricula.append(arr[inicio: inicio + tamano]) #Se recorta el segmento
        inicio += tamano #Se avanze en el indice para el proximo corte
    return cuadricula #Devuelbve la lista de segmentos








'''Pruebas locales 
ar1 = [1,2,3,4,5] 
n_c_1 = 5
c1 =  cuadricula(ar1,n_c_1)


ar2= [1,2,3,4]
n_c_2 = 5
c2 =  cuadricula(ar2,n_c_2)

ar3= [1,2,3,4]
n_c_3 = 8
c3 = cuadricula(ar3,n_c_3)


ar4= [1,2,3,4,5,6,7,8]
n_c4 = 4
c4 =  cuadricula(ar4,n_c4)



ar5= [1,2,3,4,5,6,7,8,9,10,11,12,13]
n_c5 = 5
c5 =  cuadricula(ar5,n_c5)

'''
