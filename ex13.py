from sys import argv

# script, first, second, third = argv

# print('The script is called:', script)
# print('Your first variable is:', first)
# print('Your second variable is:', second)
# print('Your third variable is:', third)

script, player1, player2, player3 = argv
rounds = int(input('How many rounds will you play? '))

print(f'So, The three players are {player1}, {player2} and {player3}. You will play {rounds} rounds!')
