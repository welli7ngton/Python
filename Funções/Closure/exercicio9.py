# Escreva uma função chamada make_timer que retorna uma função interna. A função interna deve calcular o tempo 
# decorrido desde a primeira chamada e retornar o resultado. Teste a função retornada para medir o tempo de 
# execução de diferentes partes do seu código.

import time

# inicio = time.perf_counter()

# for a in range(3):
#     time.sleep(3)

# fim = time.perf_counter()
# tempo_decorrido = fim - inicio
# tempo_decorrido = float(tempo_decorrido)
# print(f"Tempo decorrido:", {tempo_decorrido}, "segundos")

def make_timer(inicio=0, fim=0):
    
    def contador():       
        fim = time.perf_counter()
        tempo = fim - inicio
        return  tempo
    inicio = time.perf_counter()
    return contador

r = make_timer()
for a in range(2):
    time.sleep(2)
print(r())

r = make_timer()
for a in range(3):
    time.sleep(3)
print(r())

r = make_timer()
for a in range(5):
    time.sleep(1)
print(r())

# Saídas:
# 4.000861800002895
# 9.000454200002423
# 5.001692300000286