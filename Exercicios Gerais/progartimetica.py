termo = int(input("digite o primeiro termo da pa: "))
razao = int(input("digite a razao da pa: "))
num = termo
for a in range(0, 10):
    print(num)
    num = termo + razao
    termo += razao
    
