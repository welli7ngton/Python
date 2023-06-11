from sys import path

# print(*path, sep="\n")

from teste_package.produto import prod
from teste_package.subtracao import sub
from teste_package.soma import soma_dois_n


print(soma_dois_n(3,4))
print(sub(4,3))
print(prod(3,4))