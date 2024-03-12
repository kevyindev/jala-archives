import os
import random

# o desenho do robô, com marcadores de posição para os status das partes do corpo.
# colocamos 2 espadas no nosso robo.
robot_art = r"""
      0: {head_name}
      Is available: {head_status}
      Attack: {head_attack}
      Defense: {head_defense}
      Energy consumption: {head_energy_consump}
              ^
              |                  |1: {weapon_name}
              |                  |Is available: {weapon_status}
     ____     |    ____          |Attack: {weapon_attack}
    |oooo|  ____  |oooo| ------> |Defense: {weapon_defense}
    |oooo| '    ' |oooo|         |Energy consumption: {weapon_energy_consump}
    |oooo|/\_||_/\|oooo|
    `----' / __ \  `----'           |2: {left_arm_name}
   '/  |#|/\/__\/\|#|  \'           |Is available: {left_arm_status}
   /  \|#|| |/\| ||#|/  \           |Attack: {left_arm_attack}
  / \_/|_|| |/\| ||_|\_/ \          |Defense: {left_arm_defense}
 |_\/    O\=----=/O    \/_|         |Energy consumption: {left_arm_energy_consump}
 <_>      |=\__/=|      <_> ------> |
 <_>      |------|      <_>         |3: {right_arm_name}
 | |   ___|======|___   | |         |Is available: {right_arm_status}
// \\ / |O|======|O| \  //\\        |Attack: {right_arm_attack}
|  | /| |O+------+O| |  |  | /|      |Defense: {right_arm_defense}
|\/|/|\_+/        \+_/ \|\/|/ |     |Energy consumption: {right_arm_energy_consump}
\__/ |_|||        |||_\ \__/  |
     || ||        || | \     /  |6: {left_leg_name}
\   /[==|]        [|==] \   /   |Is available: {left_leg_status}
 | | [===]        [===]  | |    |Attack: {left_leg_attack}
 | |  >_<          >_<   | |    |Defense: {left_leg_defense}
 | | || ||        || ||  | |    |Energy consumption: {left_leg_energy_consump}
 | | || ||        || || -| |--> |
 \ / || ||        || ||  \ /    |7: {right_leg_name}
  |__|\_/|__    __|\_/|__ |     |Is available: {right_leg_status}
  /___n_n___\  /___n_n___\|     |Attack: {right_leg_attack}
  |                       |     |Defense: {right_leg_defense}
  |                       |     |Energy consumption: {right_leg_energy_consump}
  |                       |
  |                       |     |4: {right_sword_name}
  |                       |     |Is available: {right_sword_status}
  |                       |     |Attack: {right_sword_attack}
  |                       |     |Energy consumption: {left_sword_energy_consump}
  |                       |     |Defense: {right_sword_defense}
  |                       |     |Energy consumption: {right_sword_energy_consump}
  |-----------------------|---> |
                                |5: {left_sword_name}
                                |Is available: {left_sword_status}
                                |Attack: {left_sword_attack}
                                |Defense: {left_sword_defense}
                                |Energy consumption: {left_sword_energy_consump}
"""


##estes códigos são utilizados escrevendo-se uma “tag” que serve para sinalizar ao console que o mesmo descreve os caracteres seguintes ao invés de imprimi-los ao usuário. #ansi
colors = {
    "Black": '\033[30m',
    "Red": '\033[91m',
    "Green": '\033[92m',
    "Yellow": '\033[93m',
    "Blue": '\033[94m',
    "Magenta": '\033[95m',
    "Cyan": '\033[96m',
    "White": '\033[97m',
}

# classe representando uma parte do corpo do robô, um modelo para criar objetos.
class Part():
    def __init__(self, name, attack_level=0, defense_level=0, energy_consumption=0): #ele define as características iniciais do objeto, como o nome, níveis de ataque/defesa e consumo de energia.
        self.name = name
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.energy_consumption = energy_consumption
##estes são os atributos da classe. Eles armazenam as informações específicas de cada instância da classe.

    def get_status_dict(self):
        #aqui o nome é formatado para ser usado como chave de dicionário. os espaços serao substituídos por sublinhas e tudo é transformado em letras minúsculas.
        formatted_name = self.name.replace(" ", "_").lower()
        return {
            "{}_name".format(formatted_name): self.name.upper(),
            "{}_status".format(formatted_name): self.is_available(),
            "{}_attack".format(formatted_name): self.attack_level,
            "{}_defense".format(formatted_name): self.defense_level,
            "{}_energy_consump".format(formatted_name): self.energy_consumption,
        }
        #este é o dicionário retornado pelo método,ele contém informações formatadas sobre a parte.

    def reduce_defense(self, attack_level):

       self.defense_level = max(0, self.defense_level - attack_level)
          ##o nível de ataque recebido é subtraído do nível de defesa.

    def is_available(self):
               return self.defense_level > 0
       ##retorna se o nível de defesa for maior que zero, indicando que a parte não foi destruída.

# classe representando um robô composto por várias partes.
class Robot:
    def __init__(self, name, color_code):

        #este método define as características iniciais do robô, como nome, código de cor, energia, número de partes atacadas e uma lista de partes.
        self.name = name
        self.color_code = color_code
        self.energy = 100
        self.parts = [
            Part("Head", attack_level=5, defense_level=10, energy_consumption=5),
            Part("Weapon", attack_level=15,
                 defense_level=0, energy_consumption=10),
            Part("Left Arm", attack_level=3,
                 defense_level=20, energy_consumption=10),
            Part("Right Arm", attack_level=6,
                 defense_level=20, energy_consumption=10),
            Part("Right sword", attack_level=6,
                 defense_level=20, energy_consumption=10),
            Part("Left sword", attack_level=6,
                 defense_level=20, energy_consumption=10),
            Part("Left Leg", attack_level=4,
                 defense_level=20, energy_consumption=15),
            Part("Right Leg", attack_level=8,
                 defense_level=20, energy_consumption=50),
        ]
        #o objetivo é simular um robô com várias partes, cada uma com suas próprias características

    def print_status(self):

        #exibe o status do robô.
        print(self.color_code)
        str_robot = robot_art.format(**self.get_part_status())
        self.greet()
        self.print_energy()
        print(str_robot)
        print('\033[0m')  # Reset para a cor padrão

    def greet(self):

        ##exibe uma mensagem de saudação.
        print("Hello, my name is", self.name)

    def print_energy(self):
    #exibe o nível de energia do robô.

        print("We have", self.energy, " percent energy left")

    def get_part_status(self):

        #obtém os status de todas as partes do corpo do robô.

        part_status = {}
        for part in self.parts:
            status_dict = part.get_status_dict()
            part_status.update(status_dict)
        return part_status

    def is_there_available_part(self):

        #verifica se há pelo menos uma parte do corpo disponível no robô.
        return any(part.is_available() for part in self.parts)

    def is_on(self):

        #Verifica se o robô ainda está ativo (com energia).
        return self.energy > 0

    def attack(self, enemy_robot, part_to_use, part_to_attack):

        #realiza um ataque a uma parte do corpo do robô inimigo.
        enemy_robot.parts[part_to_attack].reduce_defense(
            self.parts[part_to_use].attack_level)
        self.energy -= self.parts[part_to_use].energy_consumption

def choose_color():
    """
    Permite ao usuário escolher uma cor para o robô.
    """
    available_colors = colors
    print("Available colors:")
    for key, value in available_colors.items():
        print(value, key)
    print(colors["Black"])
    chosen_color = input("Choose a color: ").capitalize()
    color_code = available_colors.get(chosen_color)
    if color_code is None:
        return None
    return color_code

#Constrói um robô com base nas escolhas do jogador.
def build_robot(player_number, is_ai=False):
    if is_ai:
        robot_name = random.choice(["RoboWarrior", "SteelFighter", "IronGuardian", "CyberKnight"])
        color_names = list(colors.keys())
        color_name = random.choice(color_names)
        color_code = colors[color_name]
    else:
        robot_name = input(f"Player {player_number}, enter the robot's name: ").capitalize()
        while not robot_name:
            print("Invalid name! Try again.")
            robot_name = input(f"Player {player_number}, enter the robot's name: ").capitalize()

        color_code = choose_color()
        while color_code is None:
            print("Invalid color! Try again.")
            color_code = choose_color()

    robot = Robot(robot_name, color_code)
    robot.print_status()
    return robot


def ai_choose_part(parts):
    available_parts = [index for index, part in enumerate(parts) if part.is_available()]
    return random.choice(available_parts)

def rock_paper_scissors():

    #Função para jogar pedra, papel ou tesoura e decidir quem começa.
    #Retorna True se o jogador 1 ganhar e False se o jogador 2 ganhar.
    options = ["Pedra", "Papel", "Tesoura"]
    print("Vamos decidir quem começa com Pedra, Papel ou Tesoura!")
    player1_choice = random.choice(options)
    player2_choice = random.choice(options)
    print(f"Jogador 1 escolheu: {player1_choice}")
    print(f"Jogador 2 escolheu: {player2_choice}")

    if player1_choice == player2_choice:
        print("Empate! Jogando novamente.")
        return rock_paper_scissors()
    elif (player1_choice == "Pedra" and player2_choice == "Tesoura") or \
         (player1_choice == "Papel" and player2_choice == "Pedra") or \
         (player1_choice == "Tesoura" and player2_choice == "Papel"):
        print("Jogador 1 começa!")
        return True
    else:
        print("Jogador 2 começa!")
        return False

def play():
    #Start game
    print("Welcome to the game!")

    print("\nPlayer 1:")
    robot_one = build_robot(1)

    print("\nAI Robot:")
    robot_two = build_robot(2, is_ai=True)

    player1_starts = rock_paper_scissors()

    # Escolha dos robôs
    current_robot = robot_one if player1_starts else robot_two
    enemy_robot = robot_two if player1_starts else robot_one
    # Contador de rodadas
    round_count = 0

    # Loop principal do jogo
    while robot_one.is_on() and robot_two.is_on() and robot_one.is_there_available_part() and robot_two.is_there_available_part():
        print("\nRound", round_count + 1)
        print(f"{current_robot.color_code}{current_robot.name}'s turn{colors['White']}")
        current_robot.print_status()

        if current_robot == robot_two:
            # AI's turn
            part_to_use = ai_choose_part(robot_two.parts)
            part_to_attack = ai_choose_part(robot_one.parts)
        else:
            # Human player's turn
            part_to_use = int(input("Choose the number of the part to attack with (0 to 7): "))
            while part_to_use < 0 or part_to_use > 7:
                print("Invalid part number. Please choose a number between 0 and 7.")
                part_to_use = int(input("Choose the number of the part to attack with (0 to 7): "))

            # Imprimindo o status do inimigo
            print(f"{enemy_robot.color_code}Status of {enemy_robot.name}{colors['White']}")
            enemy_robot.print_status()

            # Escolha da parte a ser atacada pelo inimigo
            part_to_attack = int(input("Choose the number of the enemy's part to attack (0 to 7): "))
            while part_to_attack < 0 or part_to_attack > 7:
                print("Invalid part number. Please choose a number between 0 and 7.")
                part_to_attack = int(input("Choose the number of the enemy's part to attack (0 to 7): "))

        # Atacando o inimigo
        current_robot.attack(enemy_robot, part_to_use, part_to_attack)
        round_count += 1

        # Imprimindo o resultado da rodada
        print("\nRound Result:")
        print(f"{current_robot.name} attacked {enemy_robot.name}'s {enemy_robot.parts[part_to_attack].name}")
        print(f"{enemy_robot.name}'s {enemy_robot.parts[part_to_attack].name} was damaged. New defense level: {enemy_robot.parts[part_to_attack].defense_level}")

        # Verificando se o inimigo ficou sem energia ou sem partes disponíveis
        if not enemy_robot.is_on() or not enemy_robot.is_there_available_part():
            print(f"\nCongratulations, {current_robot.name} wins!")
            break

        # Alternando os papéis dos robôs
        current_robot, enemy_robot = enemy_robot, current_robot

    # Imprimindo o sumário do jogo
    print("Game Summary:")
    print(f"{robot_one.name}: Energy - {robot_one.energy}%")
    print(f"{robot_two.name}: Energy - {robot_two.energy}%")

    # Imprimindo as estatísticas do jogo
    print("\nGame Statistics:")
    print(f"Total Rounds: {round_count}")

    # Imprimindo o resultado final da partida
    if robot_one.energy <= 0 and robot_two.energy <= 0:
        print("\nIt's a draw! Both robots have run out of energy.")
    elif robot_one.energy <= 0:
        print(f"\nCongratulations, {robot_two.name} wins the battle with {robot_two.energy}% energy remaining!")
    elif robot_two.energy <= 0:
        print(f"\nCongratulations, {robot_one.name} wins the battle with {robot_one.energy}% energy remaining!")

    if current_robot == robot_two:
            # AI's turn
            part_to_use = ai_choose_part(robot_two.parts)
            part_to_attack = ai_choose_part(robot_one.parts)
    else:
            # Human player's turn
            part_to_use = int(input("Escolha o número da parte para atacar (0 a 7): "))
            while part_to_use < 0 or part_to_use > 7:
                print("Número de parte inválido. Por favor, escolha um número entre 0 e 7.")
                part_to_use = int(input("Escolha o número da parte para atacar (0 a 7): "))

            print(f"{enemy_robot.color_code}Status do {enemy_robot.name}{colors['White']}")
            enemy_robot.print_status()

            part_to_attack = int(input("Escolha o número da parte para atacar no inimigo (0 a 7): "))
            while part_to_attack < 0 or part_to_attack > 7:
                print("Número de parte inválido. Por favor, escolha um número entre 0 e 7.")
                part_to_attack = int(input("Escolha o número da parte para atacar no inimigo (0 a 7): "))

    current_robot.attack(enemy_robot, part_to_use, part_to_attack)

def clear_screen():
    #esta função utiliza a biblioteca 'os' para limpar a tela do console
    os.system('cls' if os.name == 'nt' else 'clear')

def display_start_menu():
    #exibe um menu de início estilizado.
    clear_screen()
    print("********************************************")
    print("*  Welcome to the Robot Battle Game!       *")
    print("*                                          *")
    print("*  Instructions:                           *")
    print("*  1. Each player will create a robot      *")
    print("*     with different parts.                *")
    print("*  2. The game will randomly choose        *")
    print("*     who will start using the pattern     *")
    print("*     (rockpaper and scissors).            *")
    print("*     which player starts.                 *")
    print("*  3. In each round, a player will         *")
    print("*     choose a part to attack on the       *")
    print("*     opponent's robot.                    *")
    print("*  4. The attacked part's defense level    *")
    print("*     will be reduced.                     *")
    print("*  5. The game continues until one of      *")
    print("*     the robots runs out of energy        *")
    print("*     or loses all parts.                  *")
    print("*                                          *")
    print("********************************************\n")
    print("Menu:")
    print("1. Start Game")
    print("2. Quit")

    choice = input("Enter your choice (1 or 2): ")
    while choice not in ["1", "2"]: #Verifica se a escolha é válida (1 ou 2)
        print("Invalid choice. Please enter 1 to start the game or 2 to quit.")
        choice = input("Enter your choice (1 or 2): ")
    #em seguida ira chamar o play que esta aq embaixo, caso o player nao escolher 1, o jogo ira se encerrar!

    if choice == "1":
        play()
    else:
        print("Goodbye!")

if __name__ == "__main__":
    display_start_menu()
