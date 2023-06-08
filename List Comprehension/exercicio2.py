# Dada uma lista de números, filtre os números pares usando list comprehension.

l = [1,2,3,4,5,6,7,8,9]

l2 = [num for num in l if num %2 == 0]

print(l2)