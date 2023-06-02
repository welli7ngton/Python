# Crie uma função chamada make_cache que retorna uma função interna. A função interna deve armazenar em cache os 
# resultados de chamadas anteriores e retornar o resultado armazenado se a mesma entrada for fornecida 
# novamente. Teste a função retornada para evitar cálculos repetidos.

def make_cache(cache =  []):

    def salvo(novo_valor):
        
        
        cache.append(novo_valor)

        return cache
    return salvo


a = make_cache()

print(a('teste'))
print(a(1))
print(a(9.7))

# saída: 
# ['teste']
# ['teste', 1]
# ['teste', 1, 9.7]