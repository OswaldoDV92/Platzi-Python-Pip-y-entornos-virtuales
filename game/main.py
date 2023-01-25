import random

def choose_option():
    #selecciona piedra papel o tijeras
    options = ('piedra', 'papel', 'tijeras')
    user_option = input('Escoge piedra, papel o tijeras => ').lower()
    if not user_option in options:
        print('Opción inválida')
        return None, None

    computer_option = random.choice(options)
    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Empate!')

    elif user_option == 'piedra':
        if computer_option == 'tijeras':
            print('piedra gana a tijeras')
            print('Usuario gana!')
            user_wins += 1
        elif computer_option == 'papel':
            print('papel gana a piedra')
            print('Computadora gana!')
            computer_wins += 1

    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('Usuario gana!')
            user_wins += 1
        elif computer_option == 'tijeras':
            print('tijeras gana a papel')
            print('Computadora gana!')
            computer_wins += 1

    elif user_option == 'tijeras':
        if computer_option == 'papel':
            print('tijeras gana a papel')
            print('Usuario gana!')
            user_wins += 1
        elif computer_option == 'piedra':
            print('piedra gana a tijeras')
            print('Computadora gana!')
            computer_wins += 1
    return user_wins, computer_wins

def check_winner(user_wins, computer_wins, endgame):
    if user_wins == 2:
        print('El ganador es el usuario')
        endgame = False

    elif computer_wins == 2:
        print('El ganador es la computadora')
        endgame = False
    return endgame

def run_game():
    rounds = 1
    user_wins = 0
    computer_wins = 0
    endgame = True

    while endgame == True:
        print('*' * 9)
        print(' Round', rounds)
        print('*' * 9)

        print('Computer wins:', computer_wins)
        print('User wins:', user_wins)

        user_option, computer_option = choose_option()

        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        rounds += 1
        endgame = check_winner(user_wins, computer_wins, endgame)

run_game()
