# Dada uma lista de números, crie uma nova lista com os números ímpares elevados ao cubo 
# usando list comprehension.

l=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

nl = [n**3 for n in l if n %2 !=0]

print(nl)