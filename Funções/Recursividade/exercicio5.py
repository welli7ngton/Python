#5. Defina a função num_perf que recebe como argumento um número inteiro positivo e devolve True se esse número for um número perfeito e False em caso contrário. Recorde que um número perfeito é um número natural que é igual à soma de todos os seus divisores próprios, isto é, a soma de todos os divisores excluindo o próprio número. Pode, se assim o entender, definir funções auxiliares.

def num_perf(n, divisor=1, soma_divisores=0):
    if divisor >= n:  # Base case: Quando o divisor ultrapassa ou é igual ao número, verifica se a soma é igual a n
        if soma_divisores == n:
            return True
        else:
            return False
    
    if n % divisor == 0:  # Se o divisor é um divisor de n, adiciona-o à soma
        soma_divisores += divisor
    
    divisor += 1  # Incrementa o divisor
    
    return num_perf(n, divisor, soma_divisores)  # Chama recursivamente a função com os novos valores de divisor e soma_divisores

print(num_perf(7))