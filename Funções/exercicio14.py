#Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Farenheit
#ou vice-versa.Para cada opção, crie uma função. Crie uma terceira, que é um menu para o usuário escolher a opção
#desejada, onde esse menu chama a função de conversão correta.Conversão entre Celsius e Farenheit

def celtofar(tempcel):
    #(0 °C × 9/5) + 32 = 32 °F


   tempF = tempcel * 1.8 + 32

   return(tempF)

def fartocel(tempfar):
    tempC = tempfar / 1.8 - 32

    return(tempC)


tipo = input("digite F para converter de Celsius para Farenheit ou C para o contrário: ")

if tipo in "Ff":

    temperatura = float(input("digite a temperatura em Farenheit: "))
    novatemp = fartocel(temperatura)
    print(f"a temperatura {temperatura}F° equivale à: {novatemp}C°")


else:

    temperatura = float(input("digite a temperatura em Celsius: ")) 
    novatemp = celtofar(temperatura)
    print(f"a temperatura {temperatura}C° eqiovale á : {novatemp}F°")





