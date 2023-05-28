print("insira os dados de duas pessoas: ")
print("pessoa 1:")
p1_nome = input("nome: ")
p1_sexo = input("sexo: ")
p1_idade = int(input("idade: "))

print("pessoa 2:")
p2_nome = input("nome: ")
p2_sexo = input("sexo: ")
p2_idade = int(input("idade: "))

media = (p1_idade + p2_idade) / 2

print("dados:")
print(f"a pessoa 1 chamada {p1_nome}, de sexo {p1_sexo} tem {p1_idade} anos.")
print(f"a pessoa 2 chamada {p2_nome}, de sexo {p2_sexo} tem {p2_idade} anos.")

print(f"a media das idades é: {media}")