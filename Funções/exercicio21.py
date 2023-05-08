#Leia	 do	 usuário	 o	 tempo	 em	 segundos	 e	 o	 escreva	 em	 horas,	 minutos	 e	 segundos.	
#Utilize	 cinco	 métodos: para	 a	 leitura	 e	 escrita	 de	 dados e para	 obtenção	 de	 horas,	
#minutos	e	segundos	a	partir	do	tempo	em	segundos.	


def tempo(seg):

    hora = seg//3600
    resto = seg%3600

    minuto = resto//60
    segundos = resto%60

    print(hora,":",minuto,":",segundos)


duração = int(input("digite a duração em segundos: "))


tempo(duração)
