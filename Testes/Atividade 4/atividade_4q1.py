class RockPaper:
    def __init__(self) -> None:
        self.jogador1 = ''
        self.jogador2 = ''
        self.resultado = ''

    def ler_jogadas(self):
        self.jogador1 = self.menu('Jogador 1')
        self.jogador2 = self.menu('Jogador 2')

    def menu(self, jogador):
        opcoes = ['Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock']
        print(f'\n{jogador}, escolha uma opção:')
        for opcao in opcoes:
            print(f"{opcao}")
        resultado = input('Digite a opção desejada: ').capitalize()
        while resultado not in opcoes:
            print('Escolha inválida. Tente novamente.')
            resultado = input('Digite a opção desejada: ').capitalize()
        return resultado

    def determinar_vencedor(self, jogador1, jogador2):
        if jogador1 == jogador2:
            return f"\nÉ um empate! Ambos escolheram {jogador1}."
        elif (jogador1, jogador2) in [('Pedra', 'Tesoura'), ('Pedra', 'Lagarto'), ('Papel', 'Pedra'), ('Papel', 'Spock'), ('Tesoura', 'Papel'), ('Tesoura', 'Lagarto'),('Lagarto', 'Papel'), ('Lagarto', 'Spock'), ('Spock', 'Pedra'),('Spock', 'Tesoura')]:
            return f"Jogador 1 vence! ({jogador1} vence {jogador2})"
        else:
            return f"Jogador 2 vence! ({jogador2} vence {jogador1})"

    def jogar_novamente(self):
        print("\nGostaria de jogar novamente?")
        print("1: Sim ou 2: Não")
        escolha = input("Escolha uma opção: ").capitalize()
        while escolha not in ['1', '2']:
            print('Escolha inválida. Tente novamente.')
            escolha = input("Escolha uma opção: ").capitalize()
        return escolha == '1'

game = RockPaper()
while True:
    game.ler_jogadas()
    resultado = game.determinar_vencedor(game.jogador1, game.jogador2)
    print(resultado)
    if not game.jogar_novamente():
        print("\nObrigado por jogar!")
        break
