suspeita = 0
perguntas = [
    "Telefonou para a vítima? ",
    "Esteve no local do crime? ",
    "Mora perto da vítima? ",
    "Devia para a vítima? ",
    "Já trabalhou com a vítima? "]

for pergunta in perguntas:
    print(perguntas)

if suspeita == 5:
    print("Você é o assassino.")
elif suspeita >= 3:
    print("Você é considerado suspeito.")
else:
    print("Você não é considerado suspeito.")
