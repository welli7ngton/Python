#Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de
#senha incorreta informada, escrever a mensagem "Senha Invalida! Tente novamente:". Quando a senha
#for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo
#encerrado. Considere que a senha correta é o valor 2002. 


a = int(input('digite a senha: '))
while a != 2002:
    print('senha invalida')
    a = int(input()) 
print('acesso permitido')