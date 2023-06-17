# 4- Crie uma classe chamada "Temperature" com as propriedades celsius e fahrenheit. Implemente getters e setters para 
# ambas as propriedades, de modo que ao definir o valor de celsius, o valor de fahrenheit seja atualizado automaticamente 
# (e vice-versa).

# C to F
# (0 °C × 9/5) + 32 = 32 °F

# F to C
# (32 °F − 32) × 5/9 = 0 °C


class Temperature:

    def __init__(self):
        self.celsius = 0
        self.fahrenheit = 0

    
    def atualiza_farenheit(self,temp_farenheit):
        self.celsius = (temp_farenheit - 32) * (5/9)
        self.fahrenheit = temp_farenheit
        return f"temperatura em F°: {self.fahrenheit} temperatura em C°: {self.celsius}"

    def atualiza_celsius(self,temp_celsius):
        self.fahrenheit = (temp_celsius * (9/5)) + 32  
        self.celsius = temp_celsius
        return f"temperatura em C°: {self.celsius} temperatura em F°: {self.fahrenheit}"

teste = Temperature()

print(teste.atualiza_celsius(32))
print(teste.atualiza_farenheit(32))
