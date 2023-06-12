# 5- Implemente uma função chamada count_calls que retorne uma função decorada que conta o número de 
# vezes que a função decorada foi chamada. A função decorada deve imprimir o número de chamadas antes 
# de cada execução.


def count_calls(funcao,c=0):
    def decorada(*args):
        nonlocal c
        print(f'Chamada n° = {c+1}')
        c += 1
        return funcao(*args)
    return decorada

@count_calls
def cria_vetor(x):
    vet = [0 for _ in range(x)]
    return f'{vet}'


print(cria_vetor(1))
print(cria_vetor(2))
print(cria_vetor(1))
print(cria_vetor(4))
print(cria_vetor(5))
print(cria_vetor(9))
print(cria_vetor(7))
print(cria_vetor(1))
