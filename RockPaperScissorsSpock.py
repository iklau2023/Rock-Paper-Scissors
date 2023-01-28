import random
print('Welcome to rock, paper, scissors, spock, lizard')
x= input('Chose your option:').lower()
y=['rock','paper','scissors','spock','lizard']
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
elif (z=='spock' and x=='rock'):
    print('You lose, Spock disintegrates rock')
elif (z=='rock' and x=='spock'):
        print('You WIN!!!, Spock disintegrates rock')
elif (z=='spock' and x=='paper'):
    print('You WIN!!! paper disproves Spock')
elif (z=='paper' and x=='spock'):
    print('You lose, paper disproves Spock')
elif (z=='spock' and x=='scissors'):
    print('You lose Spock smashes scissors')
elif (z=='scissors' and x=='spock'):
    print('You WIN!!! Spock smashes scissors')
elif (z=='lizard' and x=='rock'):
    print('You WIN!!! rock smashes lizard')
elif (z=='rock' and x=='lizard'):
    print('You lose, rock smashes lizard')
elif (z=='lizard' and x=='paper'):
    print('You lose lizard eats paper')
elif (z=='paper' and x=='lizard'):
    print('You WIN!!! lizard eats paper')
elif (z=='lizard' and x=='scissors'):
    print('You WIN!!! scissors decapitates lizard')
elif (z=='scissors' and x=='lizard'):
    print('You lose, scissors decapitates lizard')
else:
    print('Please put rock, paper, scissors, spock, or lizard')
