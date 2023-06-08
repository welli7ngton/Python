# Dada uma lista de números, crie uma nova lista com os números maiores que 10 usando list 
# comprehension.


l = [11,12,13,14,15,6,7,8,9,10]

l2 =[n for n in l if n > 10]

print(l2)