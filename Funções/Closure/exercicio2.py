# 2 - Escreva uma função chamada counter que retorna uma função interna. A função interna deve manter uma 
# contagem interna que é incrementada toda vez que é chamada e retorna o valor da contagem atual. Teste a função 
# retornada para ver se ela conta corretamente.


def counter():
    cont = 0
    def contador():
        
        nonlocal cont
        cont += 1

        return cont
    return contador

a = counter()
b = counter()

print(a(),a(),a(),a(),a(),a(),a(),a(),a(), sep="\n") # 1 2 3 4 5 6 7 8 9 
