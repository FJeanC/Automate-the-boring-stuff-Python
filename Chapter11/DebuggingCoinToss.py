import random
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

coin = ('tails', 'heads')
guess = ''
while guess not in coin:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug("Toss: %d", toss)
if coin[toss] == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if coin[toss] == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')