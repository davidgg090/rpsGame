import random, sys

print('Roca, Papel, Tijera')

victorias = 0
perdidas = 0
empates = 0

while True:
    print('%s Victorias, %s Perdidas, %s Empates' % (victorias, perdidas, empates))
    while True:
        print('Ingrese su movimiento: (r)oca (p)apel (t)ijeras or (s)alir ')
        playerMove = input()
        if playerMove == 's':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove =='t':
            break
        print('Escriba una de estas opciones  r, p, t or q.')

    if playerMove == 'r':
        print('Roca vs ...')
    elif playerMove == 'p':
        print('Papel vs ...')
    elif playerMove == 't':
        print('Tijeras vs ...')
    
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
    elif randomNumber == 2:
        computerMove = 'p'
    elif randomNumber == 3:
        computerMove = 't'

    if playerMove == computerMove:
        print('Es un empate!')
        empates += 1

    elif playerMove == 'r' and computerMove == 't':
        print('Ganaste tu!')
        victorias += 1
    elif playerMove == 'p' and computerMove == 'r':
        print('Ganaste tu!')
        victorias += 1
    elif playerMove == 't' and computerMove == 'p':
        print('Ganaste tu!')
        victorias += 1

    elif playerMove == 'r' and computerMove == 'p':
        print('Perdiste tu!')
        perdidas += 1
    elif playerMove == 'p' and computerMove == 't':
        print('Perdiste tu!')
        perdidas += 1
    elif playerMove == 't' and computerMove == 'r':
        print('Perdiste tu!')
        perdidas += 1
    