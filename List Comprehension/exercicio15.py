# Dada uma lista de números, crie uma nova lista com os números que são múltiplos de 3 e 5 
# ao mesmo tempo usando list comprehension.


numeros = [n for n in range(101)]


nmult = [numero for numero in numeros if numero %3 == 0 and numero %5 == 0]

print(nmult)