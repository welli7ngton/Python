# 1- Escreva uma função decoradora chamada logger que registre o tempo de execução de uma função e 
# imprima no console. Use time.time() para obter o tempo inicial e final da execução.

import time


def logger(funcao):
    
    def conta_exec(*args):    
        print("inicio decoracao")
        ini = time.time()
        funcao(*args)
        fim = time.time()
        print("fim decoracao")
        return f"o tempo de execução da função foi: {round(fim - ini, 1)}"
    return conta_exec


@logger
def conta_ate_x(x):
    for i in range(x):
        time.sleep(1)


print(conta_ate_x(8))

print(conta_ate_x(10))

print(conta_ate_x(7))
