#Leia um	 número	 decimal	 (até	 3	 dígitos)	 e	 escreva	 o	 seu	 equivalente	 em	 
#numeração romana.	 Utilize	 funções	 para	 obter	 cada	 dígito	 do	 número	 decimal	 e	 para a	
#transformação	de	numeração	decimal	para	romana	(Dica1:	1	=	I,	5	=	V,	10	=	X,	50	=	L,	
#100	=	C,	500	=	D,	1.000	=	M;	Dica2:	utilize	um	vetor	guardando	a	tradução	para	
#cada um	dos	dígitos).

decimal = ["1", "5", "10", "50", "100", "500", "1000"]
romano = ["I", "V", "X", "L", "C", "D", "M"]


num = input("digite um numero com até 3 digitos: ")


def centena(numero):
    global decimal
    global romano
    
    c = int(num[0])
    c *= 100
    if c < 500:
        C = "CD"
    elif c > 499:
        C = "C"


    

    return

def dezena():
    return

def unidade():
    return

