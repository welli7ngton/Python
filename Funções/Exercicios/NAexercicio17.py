# A probabilidade de dar um valor em um dado é 1/6 (uma em 6). Faça um script
# em Python que simule 1 milhão de lançamentos de dados e mostre a frequência
# que deu para cada número. Jogando dados com o Python
import random

frequencia = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

num_lancamentos = 1000000
for _ in range(num_lancamentos):
    resultado = random.randint(1, 6)
    frequencia[resultado] += 1

for numero, contagem in frequencia.items():
    probabilidade = contagem / num_lancamentos
    print(f'Número {numero}: {contagem} vezes ({probabilidade * 100:.2f}%)')
