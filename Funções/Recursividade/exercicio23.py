# 28. Defina a função temPrimoQ que recebe como argumento uma lista de listas de números inteiros  w e 
# devolve True se alguma das sublistas  w tem um número primo e False em caso contrário.


def temPrimoQ(w):
    def primo(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    if len(w) == 0:
        return False
    
    sublist = w[0]
    for num in sublist:
        if primo(num):
            return True
    
    return temPrimoQ(w[1:])

print(temPrimoQ([[4,4,4,4],[5,4,6,7],[2,4,3]]))
print(temPrimoQ([[4,4,4,4],[4,4,4],[],[4]]))

# saída
# True
# False