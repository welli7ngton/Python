#10. Defina a função prod_lista que recebe como argumento uma lista de inteiros e devolve o produto dos seus elementos.

def prod_lista(lista):
    if len(lista) == 0:  
        return 1
    
    primeiro_elemento = lista[0]  
    resto_da_lista = lista[1:]  
    
    return primeiro_elemento * prod_lista(resto_da_lista)  

print(prod_lista([1,2, 3, 4, 5 , 6]))


