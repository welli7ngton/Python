# Dada uma lista de números, crie uma nova lista com os números positivos convertidos em 
# floats e os números negativos convertidos em strings com um sinal negativo usando list 
# comprehension.

numeros = [-1,2,-3,4,-5,6,-7,8,-9]

nl = [
    str(num) if num < 0 else float(num)
    for num in numeros 
]

print(nl)