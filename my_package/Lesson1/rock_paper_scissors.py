player1_choice = input('Enter your choice (Rock, Paper, Scissors): ')
player2_choice = input('Enter your choice (Rock, Paper, Scissors): ')

def rockPaperScissors(player1_choice, player2_choice):
    choices = ['Rock', 'Paper', 'Scissors']

    if player1_choice == player2_choice:
        print('It is tie!')
    elif not(player1_choice in choices) or not(player2_choice in choices):
        print('Invalid Input!')
    elif (player1_choice == 'Rock' and player2_choice == 'Scissors') or (player1_choice == 'Scissors' and player2_choice == 'Paper') or (player1_choice == 'Paper' and player2_choice == 'Rock'):
        print('Player 1 Won!')
    else:
        print('Player 2 Won!')


rockPaperScissors(player1_choice, player2_choice)