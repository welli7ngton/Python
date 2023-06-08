# Dada uma lista de números, crie uma nova lista com os números negativos multiplicados por 
# 2 e os positivos divididos por 2 usando list comprehension.

l = [1,2,3,4,5,6,7,-1,-2,-3,-4,-5,-6,-7]



l2 = [n * 2 if n < 0 else n /2 for n in l]

print(l2)