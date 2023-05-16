# 3. Defina a função prim_alg que recebe como argumento um número natural e devolve o primeiro algarismo (o mais 
# significativo) na representação decimal de  n

def prim_alg(n):
    novon = str(n)
    if len(novon) == 1:
        return novon
    else:

        ultpos = len(novon) - 1
        novon2 = novon.replace(novon[ultpos], "")
        return prim_alg(int(novon2))
    
print(prim_alg(5629))

