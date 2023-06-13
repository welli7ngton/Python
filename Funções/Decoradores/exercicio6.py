# 6- Crie uma função decoradora chamada timer que calcule o tempo de execução de uma função e 
# imprima o resultado em milissegundos. A função decorada deve retornar o resultado original da função.

import time

def timer(funcao):
    
   
    def decorada(*args):
        inicio = round(time.time(),2)
        funcao(*args)
        fim = round(time.time(),2)
        
        return f"tempo de execução: {round(fim - inicio)}s"
    return decorada

@timer
def contagem_regressiva(x):
    for a in range(x+1,0,-1):
        print(x, end=" ")
        x-=1
        time.sleep(1)
    print("\n")
    


print(contagem_regressiva(5))

print(contagem_regressiva(10))