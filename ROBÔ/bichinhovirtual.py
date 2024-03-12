class AnimalVirtual:
    def __init__(self, nome, idade_bichinho, humor):
        self.nome = nome
        self.idade_bichinho = idade_bichinho
        self.humor = humor
        self.lanchinho = 0
        self.saude = 0

    def criarbichinhovirtual(self):
        print(f"Nome do bichinho: {self.nome}")
        print(f"Idade do bichinho: {self.idade_bichinho}")
        print(f"Humor do bichinho: {self.humor}")
        print("Bichinho criado com sucesso")

    def darcomida(self):
        perguntas = ["Você quer dar comida para o bichinho? "]
        for pergunta in perguntas:
            resposta = input(pergunta)
            if resposta.lower() == "sim":
                self.lanchinho += 1
                self.saude += 1
                print(f"Você alimentou o bichinho {self.lanchinho} vezes.")
            elif resposta.lower() == "não":
                self.saude -= 1
                break
            else:
                print("Resposta inválida!")

    def humorbichinho(self):
        if self.lanchinho > 0:
            humor = "feliz"
        else:
            humor = "triste"
        if self.saude <= 0:
            humor = "muito triste"
        print(f"O bichinho está {humor}. Saúde: {self.saude}")
        return humor

# Captura de informações do usuário
nome_bichinho = input("Digite o nome do bichinho: ")
idade_bichinho = int(input("Digite a idade do bichinho: "))
humor_inicial = input("Digite o humor inicial do bichinho (feliz, triste ou muito triste): ")

# Exemplo de uso
bichinho = AnimalVirtual(nome_bichinho, idade_bichinho, humor_inicial)
bichinho.criarbichinhovirtual()

while True:
    bichinho.darcomida()
    bichinho.humorbichinho()
    
    # Verifica se o bichinho está "feliz" ou "triste" com base no humor retornado pela função
    if bichinho.humorbichinho() == "feliz":
        print("O bichinho está feliz!")
    elif bichinho.humorbichinho() == "triste":
        print("O bichinho está triste.")
    else:
        print("O bichinho está muito triste.")

    continuar = input("Deseja continuar alimentando o bichinho? (sim/não) ")
    if continuar.lower() != "sim":
        break
