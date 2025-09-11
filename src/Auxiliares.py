def k_merge(listas):
    """
    Recibe una lista de k listas ordenadas
    y regresa una sola lista con todos los elementos

    """
    
    if not listas:
        return []    

    resultado = []
    for lista in listas:
        resultado.extend(lista)
    
    resultado.sort()
    return resultado

def cuadricula(arr,cantidad_nodos):
    longitud = len(arr)
    base = longitud // cantidad_nodos
    residuo = longitud % cantidad_nodos

    cuadricula = []
    inicio = 0
    for i in range(cantidad_nodos):
        tamano = base +(1 if i < residuo else 0)
        cuadricula.append(arr[inicio: inicio + tamano])
        inicio += tamano
    return cuadricula








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
