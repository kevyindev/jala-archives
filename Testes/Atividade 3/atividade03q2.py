#Em uma cidade do Canadá com climas frios na maioria das vezes, é necessário saber quando você pode sair sem 
#precisar usar casacos, ou seja, quando há sol. Para isso, foi solicitado que você realizasse um programa
# que determina se as pessoas podem sair sem problemas, então apresentamos a função input.

class WeatherMachine:
    def __init__(self):
        pass

    def fahrenheitcelsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius

    def get_weather(self, temperature_fahrenheit):
        celsius = self.fahrenheitcelsius(temperature_fahrenheit)
        print(f"A temperatura em celsius é: {celsius:.2f}C°")
        if temperature_fahrenheit >= 65:
            print("O clima é ideal para sair sem casaco.")
        else:
            print("Fique em casa, está frio lá fora.")

weather_machine = WeatherMachine()
temperature_input = float(input("Digite a temperatura em graus Fahrenheit: "))
weather_machine.get_weather(temperature_input)