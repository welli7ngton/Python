casos = int(input("digite quantos casos voce vai digitar: "))



pesos = 10

for a in range(0, casos):
    print("digite os três numeros: ")
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    
    n1 = n1 * 2
    n2 = n2 * 3
    n3 = n3 * 5

    media = (n1 + n2 + n3)/pesos
    print(f"MEDIA = {media:.1f}")
    