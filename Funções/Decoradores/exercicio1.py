# 1- Escreva uma função decoradora chamada logger que registre o tempo de execução de uma função e 
# imprima no console. Use time.time() para obter o tempo inicial e final da execução.

import time


def logger(funcao):
    ini = time.time()
    def conta_exec():
        nonlocal ini,funcao
        print("inicio decoracao")
        funcao()
        fim = time.time()
        print("fim decoracao")
        return f"o tempo de execução da função foi: {round(fim - ini, 1)}"
    return conta_exec




@logger
def conta_ate_10():  
    for i in range(10):
        time.sleep(1)

@logger
def conta_ate_5():
    for i in range(5):
        time.sleep(1)

print(conta_ate_5())
print(conta_ate_10())


