import random
print('Welcome to Rock, Paper, Scissors, Shoot')
x= input('Chose your option:').lower()
y=['rock','paper','scissors']
z= random.choice(y)
if (x == z):
    print('Tie')
elif (z == 'paper' and x == 'rock'):
    print('You lose, paper beats rock')
elif (z == 'rock' and x == 'paper'):
    print('You WIN!!!, paper beats rock')
elif (z == 'scissors' and x == 'paper'):
    print('You lose, scissors beat paper')
elif (z == 'paper' and x == 'scissors'):
    print('You WIN!!!, scissors beat paper')
elif (z == 'rock' and x == 'scissors'):
    print('You lose, rock beats scissors')
elif (z == 'scissors' and x == 'rock'):
    print("You WIN!!!, rock beats scissors")
else:
    print('Please put rock, paper, or scissors')