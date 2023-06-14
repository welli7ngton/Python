# 8- Implemente uma função decoradora chamada retry_with_backoff que execute uma função novamente se ela lançar 
# uma exceção, com um intervalo de tempo crescente entre as tentativas. A função decoradora deve aceitar o número 
# máximo de tentativas e o fator de aumento do intervalo de espera como argumentos.

import time

def retry_with_backoff(max_tent,fator_aumento):
    def executa(funcao):
        c = 1
        def decoradora(*args):
            nonlocal c
            try:
                print(funcao(*args))
            except ZeroDivisionError:
                while c <= max_tent:
                    print(f"Tentativa n° = {c}")
                    print(f"Erro, tentando novamente em {c*fator_aumento}s")
                    c += 1
                    time.sleep(c*fator_aumento)
                    decoradora(*args)

        return decoradora
    return executa

@retry_with_backoff(max_tent=3,fator_aumento=2)
def divisao(x,y):
    return x/y

divisao(10,0)

print()

divisao(5,0)