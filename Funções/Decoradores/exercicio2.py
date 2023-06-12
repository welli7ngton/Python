# 2- Implemente uma função decoradora chamada retry que execute uma função novamente se ela lançar 
# uma exceção específica. A função decoradora deve aceitar o número máximo de tentativas e o tempo 
# de espera entre cada tentativa como argumentos.

import time

def retry(max_tentativas,tempo_espera):
    def decoradora(funcao):
        def execucoes(*args,**kwargs):
            tentativas = 0
            while tentativas < max_tentativas:
                try:
                    return funcao(*args,**kwargs)
                except Exception as e:
                    tentativas += 1
                    print(f"Ocorreu uma exceção: {e}, tentando novamente em {tempo_espera} segundos.")
                    time.sleep(tempo_espera)
            raise Exception(f"Máximo de tentativas alcançado ({max_tentativas}).")
        return execucoes
    return decoradora



@retry(max_tentativas=5,tempo_espera=3)
def divisao(x,y):
    return x/y

print(divisao(10,"l"))